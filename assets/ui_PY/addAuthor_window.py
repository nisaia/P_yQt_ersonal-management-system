# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_XML/addAuthor_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addAuthor_window(object):
    def setupUi(self, addAuthor_window):
        addAuthor_window.setObjectName("addAuthor_window")
        addAuthor_window.resize(890, 730)
        addAuthor_window.setStyleSheet("QLabel#addAuthor_label {\n"
"    background-color: green;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(addAuthor_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(addAuthor_window)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.authorName_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.authorName_label.setFont(font)
        self.authorName_label.setObjectName("authorName_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.authorName_label)
        self.authorName_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.authorName_lineEdit.setObjectName("authorName_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.authorName_lineEdit)
        self.authorSurname_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.authorSurname_label.setFont(font)
        self.authorSurname_label.setObjectName("authorSurname_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.authorSurname_label)
        self.authorSurname_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.authorSurname_lineEdit.setObjectName("authorSurname_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.authorSurname_lineEdit)
        self.addAuthor_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addAuthor_button.setFont(font)
        self.addAuthor_button.setObjectName("addAuthor_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.addAuthor_button)
        self.clearAll_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clearAll_button.setFont(font)
        self.clearAll_button.setObjectName("clearAll_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.clearAll_button)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(addAuthor_window)
        QtCore.QMetaObject.connectSlotsByName(addAuthor_window)

    def retranslateUi(self, addAuthor_window):
        _translate = QtCore.QCoreApplication.translate
        addAuthor_window.setWindowTitle(_translate("addAuthor_window", "Form"))
        self.authorName_label.setText(_translate("addAuthor_window", "Name:"))
        self.authorSurname_label.setText(_translate("addAuthor_window", "Surname:"))
        self.addAuthor_button.setText(_translate("addAuthor_window", "Add author"))
        self.clearAll_button.setText(_translate("addAuthor_window", "Clear all"))
        self.label.setText(_translate("addAuthor_window", "Add author"))
