import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from book_management_system.ui.addAuthor_window import *
from database.db import book_session
from database.book_models import Author
from utils.custom_exceptions import *
from utils.functions import openDialog

class AddAuthorView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_addAuthor_window()
        self.ui.setupUi(self)


        self.ui.addAuthor_button_1.clicked.connect(self.addAuthor)
        self.ui.clearAll_button.clicked.connect(self.clearAll)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()


    def addAuthor(self):
        try:
            name = self.ui.authorName_lineEdit.text()
            surname = self.ui.authorSurname_lineEdit.text()

            if len(name) == 0: raise NoInputException('Enter author name')
            if len(surname) == 0: raise NoInputException('Enter author surname')

            author = Author(name=name, surname=surname)
            book_session.add(author)
            book_session.commit()

            self.clearAll()
            openDialog(QMessageBox.Information, 'Author inserted', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')

    def clearAll(self):
        self.ui.authorName_lineEdit.clear()
        self.ui.authorSurname_lineEdit.clear()