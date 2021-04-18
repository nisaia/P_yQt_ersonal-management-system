# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_XML/book_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_book_window(object):
    def setupUi(self, book_window):
        book_window.setObjectName("book_window")
        book_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(book_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(book_window)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.isbn = QtWidgets.QLabel(self.tab)
        self.isbn.setAlignment(QtCore.Qt.AlignCenter)
        self.isbn.setObjectName("isbn")
        self.gridLayout.addWidget(self.isbn, 1, 1, 1, 1)
        self.category = QtWidgets.QLabel(self.tab)
        self.category.setAlignment(QtCore.Qt.AlignCenter)
        self.category.setObjectName("category")
        self.gridLayout.addWidget(self.category, 3, 1, 1, 1)
        self.description = QtWidgets.QLabel(self.tab)
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 4, 0, 1, 2)
        self.title = QtWidgets.QLabel(self.tab)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        self.author = QtWidgets.QLabel(self.tab)
        self.author.setAlignment(QtCore.Qt.AlignCenter)
        self.author.setObjectName("author")
        self.gridLayout.addWidget(self.author, 2, 1, 1, 1)
        self.cover = QtWidgets.QLabel(self.tab)
        self.cover.setAlignment(QtCore.Qt.AlignCenter)
        self.cover.setObjectName("cover")
        self.gridLayout.addWidget(self.cover, 0, 0, 4, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout.setObjectName("formLayout")
        self.editBook_label = QtWidgets.QLabel(self.tab_2)
        self.editBook_label.setAlignment(QtCore.Qt.AlignCenter)
        self.editBook_label.setObjectName("editBook_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.editBook_label)
        self.bookTitle_label = QtWidgets.QLabel(self.tab_2)
        self.bookTitle_label.setObjectName("bookTitle_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bookTitle_label)
        self.bookTitle_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.bookTitle_lineEdit.setObjectName("bookTitle_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bookTitle_lineEdit)
        self.isbn_label = QtWidgets.QLabel(self.tab_2)
        self.isbn_label.setObjectName("isbn_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.isbn_label)
        self.isbn_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.isbn_lineEdit.setObjectName("isbn_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.isbn_lineEdit)
        self.author_label = QtWidgets.QLabel(self.tab_2)
        self.author_label.setObjectName("author_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.author_label)
        self.author_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.author_comboBox.setObjectName("author_comboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.author_comboBox)
        self.category_label = QtWidgets.QLabel(self.tab_2)
        self.category_label.setObjectName("category_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.category_label)
        self.category_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.category_comboBox.setObjectName("category_comboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.category_comboBox)
        self.cover_label = QtWidgets.QLabel(self.tab_2)
        self.cover_label.setObjectName("cover_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.cover_label)
        self.uploadCover_button = QtWidgets.QPushButton(self.tab_2)
        self.uploadCover_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.uploadCover_button.setObjectName("uploadCover_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.uploadCover_button)
        self.coverPath_label = QtWidgets.QLabel(self.tab_2)
        self.coverPath_label.setText("")
        self.coverPath_label.setObjectName("coverPath_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.coverPath_label)
        self.preview_button = QtWidgets.QPushButton(self.tab_2)
        self.preview_button.setObjectName("preview_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.preview_button)
        self.description_label = QtWidgets.QLabel(self.tab_2)
        self.description_label.setObjectName("description_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.description_label)
        self.description_plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.description_plainTextEdit.setObjectName("description_plainTextEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.description_plainTextEdit)
        self.editBook_button = QtWidgets.QPushButton(self.tab_2)
        self.editBook_button.setObjectName("editBook_button")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.editBook_button)
        self.deleteBook_button = QtWidgets.QPushButton(self.tab_2)
        self.deleteBook_button.setObjectName("deleteBook_button")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.deleteBook_button)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(book_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(book_window)

    def retranslateUi(self, book_window):
        _translate = QtCore.QCoreApplication.translate
        book_window.setWindowTitle(_translate("book_window", "Form"))
        self.isbn.setText(_translate("book_window", "ISBN"))
        self.category.setText(_translate("book_window", "Category"))
        self.description.setText(_translate("book_window", "Description"))
        self.title.setText(_translate("book_window", "Title"))
        self.author.setText(_translate("book_window", "Author"))
        self.cover.setText(_translate("book_window", "Cover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("book_window", "Details"))
        self.editBook_label.setText(_translate("book_window", "Edit book"))
        self.bookTitle_label.setText(_translate("book_window", "Title:"))
        self.isbn_label.setText(_translate("book_window", "ISBN:"))
        self.author_label.setText(_translate("book_window", "Author:"))
        self.category_label.setText(_translate("book_window", "Category:"))
        self.cover_label.setText(_translate("book_window", "Cover:"))
        self.uploadCover_button.setText(_translate("book_window", "..."))
        self.preview_button.setText(_translate("book_window", "Preview"))
        self.description_label.setText(_translate("book_window", "Description:"))
        self.editBook_button.setText(_translate("book_window", "Edit book"))
        self.deleteBook_button.setText(_translate("book_window", "Delete book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("book_window", "Edit/Delete"))