# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_management_system/assets/XML/allMovies_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allMovies_window(object):
    def setupUi(self, allMovies_window):
        allMovies_window.setObjectName("allMovies_window")
        allMovies_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(allMovies_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.allMovies_label = QtWidgets.QLabel(allMovies_window)
        self.allMovies_label.setAlignment(QtCore.Qt.AlignCenter)
        self.allMovies_label.setObjectName("allMovies_label")
        self.verticalLayout.addWidget(self.allMovies_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.searchMovie_lineEdit = QtWidgets.QLineEdit(allMovies_window)
        self.searchMovie_lineEdit.setPlaceholderText('Search movie by [Title - Film director - Genre]')
        self.searchMovie_lineEdit.setObjectName("searchMovie_lineEdit")
        self.verticalLayout.addWidget(self.searchMovie_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.allMovies_tableView = QtWidgets.QTableView(allMovies_window)
        self.allMovies_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.allMovies_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.allMovies_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.allMovies_tableView.verticalHeader().setVisible(False)
        self.allMovies_tableView.setCursor(QtCore.Qt.PointingHandCursor)
        self.allMovies_tableView.setObjectName("allMovies_tableView")
        self.verticalLayout.addWidget(self.allMovies_tableView)

        self.retranslateUi(allMovies_window)
        QtCore.QMetaObject.connectSlotsByName(allMovies_window)

    def retranslateUi(self, allMovies_window):
        _translate = QtCore.QCoreApplication.translate
        allMovies_window.setWindowTitle(_translate("allMovies_window", "Form"))
        self.allMovies_label.setText(_translate("allMovies_window", "All movies"))
