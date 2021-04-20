# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_XML/statistics_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statistics_window(object):
    def setupUi(self, statistics_window):
        statistics_window.setObjectName("statistics_window")
        statistics_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(statistics_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.categories_labes = QtWidgets.QLabel(statistics_window)
        self.categories_labes.setAlignment(QtCore.Qt.AlignCenter)
        self.categories_labes.setObjectName("categories_labes")
        self.gridLayout.addWidget(self.categories_labes, 0, 2, 1, 1)
        self.authors_label = QtWidgets.QLabel(statistics_window)
        self.authors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.authors_label.setObjectName("authors_label")
        self.gridLayout.addWidget(self.authors_label, 0, 1, 1, 1)
        self.categories_counter_label = QtWidgets.QLabel(statistics_window)
        self.categories_counter_label.setText("")
        self.categories_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.categories_counter_label.setObjectName("categories_counter_label")
        self.gridLayout.addWidget(self.categories_counter_label, 1, 2, 1, 1)
        self.books_counter_label = QtWidgets.QLabel(statistics_window)
        self.books_counter_label.setText("")
        self.books_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.books_counter_label.setObjectName("books_counter_label")
        self.gridLayout.addWidget(self.books_counter_label, 1, 0, 1, 1)
        self.authors_counter_label = QtWidgets.QLabel(statistics_window)
        self.authors_counter_label.setText("")
        self.authors_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.authors_counter_label.setObjectName("authors_counter_label")
        self.gridLayout.addWidget(self.authors_counter_label, 1, 1, 1, 1)
        self.books_label = QtWidgets.QLabel(statistics_window)
        self.books_label.setAlignment(QtCore.Qt.AlignCenter)
        self.books_label.setObjectName("books_label")
        self.gridLayout.addWidget(self.books_label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pieChart_container = QtWidgets.QWidget(statistics_window)
        self.pieChart_container.setObjectName("pieChart_container")
        self.horizontalLayout.addWidget(self.pieChart_container)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(statistics_window)
        QtCore.QMetaObject.connectSlotsByName(statistics_window)

    def retranslateUi(self, statistics_window):
        _translate = QtCore.QCoreApplication.translate
        statistics_window.setWindowTitle(_translate("statistics_window", "Form"))
        self.categories_labes.setText(_translate("statistics_window", "Categories"))
        self.authors_label.setText(_translate("statistics_window", "Authors"))
        self.books_label.setText(_translate("statistics_window", "Books"))