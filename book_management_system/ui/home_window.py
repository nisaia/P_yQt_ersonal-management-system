# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_management_system/assets/XML/home_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home_window(object):
    def setupUi(self, home_window):
        home_window.setObjectName("home_window")
        home_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(home_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_label = QtWidgets.QLabel(home_window)
        self.home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_label.setObjectName("home_label")
        self.verticalLayout.addWidget(self.home_label)

        self.retranslateUi(home_window)
        QtCore.QMetaObject.connectSlotsByName(home_window)

    def retranslateUi(self, home_window):
        _translate = QtCore.QCoreApplication.translate
        home_window.setWindowTitle(_translate("home_window", "Form"))
        self.home_label.setText(_translate("home_window", "Home"))
