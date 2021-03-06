import sys
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QMainWindow, QDialog
from book_management_system.ui.addBook_window import *
from database.db import book_session
from database.book_models import *
from utils.custom_exceptions import NoInputException, NoNumericInputException
from sqlalchemy.exc import IntegrityError
from utils.constants import COVER_PATH, NO_COVER_AVAILABLE_PATH, FIRST_YEAR_BOOK, ACTUAL_YEAR
from os.path import join
from PyQt5.QtCore import QUrl
import shutil
from utils.functions import openDialog, displayCover, get_image_file

class AddBookView(QWidget):
    
    def __init__(self, parent):

        self.file_name = ""

        super().__init__(parent)
        self.ui = Ui_addBook_window()
        self.ui.setupUi(self)

        
        self.ui.uploadCover_button.clicked.connect(lambda: get_image_file(parent=self, label=self.ui.bookCoverPath_label, button=self.ui.bookPreview_button))
        self.ui.bookPreview_button.clicked.connect(lambda: displayCover(label=self.ui.bookCoverPath_label))
                
        self.ui.addBook_button_1.clicked.connect(self.addBook)
        self.ui.clearAll_button.clicked.connect(self.clearAll)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def updateComboBox(self):
        self.ui.bookYear_comboBox.clear()
        self.ui.bookAuthor_comboBox.clear()
        self.ui.bookGenre_comboBox.clear()
        self.ui.bookStatus_comboBox.clear()

        for year in range(FIRST_YEAR_BOOK, ACTUAL_YEAR + 1):
            self.ui.bookYear_comboBox.addItem(str(year))

        authors = book_session.query(Author).all()
        if len(authors) == 0:
            self.ui.bookAuthor_comboBox.addItem('No authors founded')
            self.ui.bookAuthor_comboBox.setDisabled(True)
        else:
            for author in authors:
                self.ui.bookAuthor_comboBox.addItem(str(author.name + " " + author.surname))
            self.ui.bookAuthor_comboBox.setDisabled(False)

        genres = book_session.query(Genre).all()
        if len(genres) == 0:
            self.ui.bookGenre_comboBox.addItem('No genres founded')
            self.ui.bookGenre_comboBox.setDisabled(True)
        else:
            for genre in genres:
                self.ui.bookGenre_comboBox.addItem(genre.name)
            self.ui.bookGenre_comboBox.setDisabled(False)

        status = book_session.query(BookStatus).all()
        for stat in status:
            self.ui.bookStatus_comboBox.addItem(stat.name)

    def addBook(self):
        try:
            book_title = self.ui.bookTitle_lineEdit.text()
            isbn = self.ui.bookIsbn_lineEdit.text()
            pages = self.ui.bookPages_lineEdit.text()
            year = int(self.ui.bookYear_comboBox.currentText())
            author = book_session.query(Author).filter_by(id=self.ui.bookAuthor_comboBox.currentIndex() + 1).first()
            genre = book_session.query(Genre).filter_by(id=self.ui.bookGenre_comboBox.currentIndex() + 1).first()
            cover_path = self.ui.bookCoverPath_label.text()
            description = self.ui.bookDescription_plainTextEdit.toPlainText()
            status = book_session.query(BookStatus).filter_by(id=self.ui.bookStatus_comboBox.currentIndex() + 1).first()


            if len(book_title) == 0: raise NoInputException('Enter the title of book')
            elif len(isbn) == 0: raise NoInputException('Enter the ISBN of book')
            elif len(pages) == 0: raise NoInputException('Enter book number pages')
            elif author == None: raise NoInputException('Enter the author of the book')
            elif genre == None: raise NoInputException('Enter the genre of the book')

            if not pages.isdigit(): raise NoNumericInputException('Pages value not valid')
            
            if len(cover_path) == 0:
                new_cover_path = NO_COVER_AVAILABLE_PATH
            else:
                file_name = QUrl.fromLocalFile(cover_path).fileName()
                new_cover_path = join(COVER_PATH, file_name)
                shutil.copy(cover_path, new_cover_path)

            print(new_cover_path)

            book = Book(title=book_title,
                        isbn=isbn,
                        pages=pages,
                        year=year,
                        author_id=author.id,
                        genre_id=genre.id,
                        description=description,
                        status_id=status.id,
                        cover_path=new_cover_path)
            
            book_session.add(book)
            book_session.commit()

            #results = session.query(Book, Author, Category).select_from(Book).join(Author).join(Category).all()
            #print(session.query(Book).join(Book.category_id).join(Book.author_id)).all()
            #for book, author, category in results:
                #print(book.title, author.name, author.surname, category.name)

            self.clearAll()

            openDialog(QMessageBox.Information, 'Book added', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except NoNumericInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Book already inserted', 'Error')
            book_session.rollback()

    def clearAll(self):
        self.ui.bookTitle_lineEdit.clear()
        self.ui.bookIsbn_lineEdit.clear()
        self.ui.bookYear_comboBox.setCurrentIndex(0)
        self.ui.bookAuthor_comboBox.setCurrentIndex(0)
        self.ui.bookGenre_comboBox.setCurrentIndex(0)
        self.ui.bookCoverPath_label.setText("")
        self.ui.bookPages_lineEdit.clear()
        self.ui.bookCoverPath_label.setVisible(False)
        self.ui.bookPreview_button.setVisible(False)
        self.ui.bookDescription_plainTextEdit.clear()
        self.ui.bookStatus_comboBox.setCurrentIndex(0)