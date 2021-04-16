# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_XML/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setObjectName("home_button")
        self.verticalLayout.addWidget(self.home_button)
        self.addBook_button = QtWidgets.QPushButton(self.centralwidget)
        self.addBook_button.setObjectName("addBook_button")
        self.verticalLayout.addWidget(self.addBook_button)
        self.allBooks_button = QtWidgets.QPushButton(self.centralwidget)
        self.allBooks_button.setObjectName("allBooks_button")
        self.verticalLayout.addWidget(self.allBooks_button)
        self.addAuthor_button = QtWidgets.QPushButton(self.centralwidget)
        self.addAuthor_button.setObjectName("addAuthor_button")
        self.verticalLayout.addWidget(self.addAuthor_button)
        self.addCategory_button = QtWidgets.QPushButton(self.centralwidget)
        self.addCategory_button.setObjectName("addCategory_button")
        self.verticalLayout.addWidget(self.addCategory_button)
        self.statistics_button = QtWidgets.QPushButton(self.centralwidget)
        self.statistics_button.setObjectName("statistics_button")
        self.verticalLayout.addWidget(self.statistics_button)
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout.addWidget(self.settings_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_button.setText(_translate("MainWindow", "Home"))
        self.addBook_button.setText(_translate("MainWindow", "Add book"))
        self.allBooks_button.setText(_translate("MainWindow", "All books"))
        self.addAuthor_button.setText(_translate("MainWindow", "Add author"))
        self.addCategory_button.setText(_translate("MainWindow", "Add category"))
        self.statistics_button.setText(_translate("MainWindow", "Statistics"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
