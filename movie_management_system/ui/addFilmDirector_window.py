# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_management_system/assets/XML/addFilmDirector_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addFilmDirector_window(object):
    def setupUi(self, addFilmDirector_window):
        addFilmDirector_window.setObjectName("addFilmDirector_window")
        addFilmDirector_window.resize(890, 730)
        self.formLayout = QtWidgets.QFormLayout(addFilmDirector_window)
        self.formLayout.setObjectName("formLayout")
        self.filmDirectorName_label = QtWidgets.QLabel(addFilmDirector_window)
        self.filmDirectorName_label.setObjectName("filmDirectorName_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.filmDirectorName_label)
        self.addFilmDirector_label = QtWidgets.QLabel(addFilmDirector_window)
        self.addFilmDirector_label.setAlignment(QtCore.Qt.AlignCenter)
        self.addFilmDirector_label.setObjectName("addFilmDirector_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.addFilmDirector_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.filmDirectorName_lineEdit = QtWidgets.QLineEdit(addFilmDirector_window)
        self.filmDirectorName_lineEdit.setObjectName("filmDirectorName_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.filmDirectorName_lineEdit)
        self.filmDirectorSurame_label = QtWidgets.QLabel(addFilmDirector_window)
        self.filmDirectorSurame_label.setObjectName("filmDirectorSurame_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.filmDirectorSurame_label)
        self.filmDirectorSurname_lineEdit = QtWidgets.QLineEdit(addFilmDirector_window)
        self.filmDirectorSurname_lineEdit.setObjectName("filmDirectorSurname_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.filmDirectorSurname_lineEdit)
        self.addFilmDirector_button_1 = QtWidgets.QPushButton(addFilmDirector_window)
        self.addFilmDirector_button_1.setObjectName("addFilmDirector_button_1")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.addFilmDirector_button_1)
        self.clearAll_button = QtWidgets.QPushButton(addFilmDirector_window)
        self.clearAll_button.setObjectName("clearAll_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.clearAll_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.SpanningRole, spacerItem1)

        self.retranslateUi(addFilmDirector_window)
        QtCore.QMetaObject.connectSlotsByName(addFilmDirector_window)

    def retranslateUi(self, addFilmDirector_window):
        _translate = QtCore.QCoreApplication.translate
        addFilmDirector_window.setWindowTitle(_translate("addFilmDirector_window", "Form"))
        self.filmDirectorName_label.setText(_translate("addFilmDirector_window", "Name:"))
        self.addFilmDirector_label.setText(_translate("addFilmDirector_window", "Add film director"))
        self.filmDirectorSurame_label.setText(_translate("addFilmDirector_window", "Surname:"))
        self.addFilmDirector_button_1.setText(_translate("addFilmDirector_window", "Add film director"))
        self.clearAll_button.setText(_translate("addFilmDirector_window", "Clear all"))
