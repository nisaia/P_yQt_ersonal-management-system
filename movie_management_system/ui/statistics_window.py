# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_management_system/assets/XML/statistics_window.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(statistics_window)
        self.gridLayout.setObjectName("gridLayout")
        self.filmDirectors_label = QtWidgets.QLabel(statistics_window)
        self.filmDirectors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filmDirectors_label.setObjectName("filmDirectors_label")
        self.gridLayout.addWidget(self.filmDirectors_label, 0, 1, 1, 1)
        self.movies_label = QtWidgets.QLabel(statistics_window)
        self.movies_label.setAlignment(QtCore.Qt.AlignCenter)
        self.movies_label.setObjectName("movies_label")
        self.gridLayout.addWidget(self.movies_label, 0, 0, 1, 1)
        self.genres_label = QtWidgets.QLabel(statistics_window)
        self.genres_label.setAlignment(QtCore.Qt.AlignCenter)
        self.genres_label.setObjectName("genres_label")
        self.gridLayout.addWidget(self.genres_label, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 3)
        self.filmDirectorsCounter_label = QtWidgets.QLabel(statistics_window)
        self.filmDirectorsCounter_label.setText("")
        self.filmDirectorsCounter_label.setObjectName("filmDirectorsCounter_label")
        self.gridLayout.addWidget(self.filmDirectorsCounter_label, 1, 1, 1, 1)
        self.moviesCounter_label = QtWidgets.QLabel(statistics_window)
        self.moviesCounter_label.setText("")
        self.moviesCounter_label.setObjectName("moviesCounter_label")
        self.gridLayout.addWidget(self.moviesCounter_label, 1, 0, 1, 1)
        self.genresCounter_label = QtWidgets.QLabel(statistics_window)
        self.genresCounter_label.setText("")
        self.genresCounter_label.setObjectName("genresCounter_label")
        self.gridLayout.addWidget(self.genresCounter_label, 1, 2, 1, 1)
        self.pieChart_container = QtWidgets.QHBoxLayout()
        self.pieChart_container.setObjectName("pieChart_container")
        self.gridLayout.addLayout(self.pieChart_container, 3, 0, 1, 3)

        self.retranslateUi(statistics_window)
        QtCore.QMetaObject.connectSlotsByName(statistics_window)

    def retranslateUi(self, statistics_window):
        _translate = QtCore.QCoreApplication.translate
        statistics_window.setWindowTitle(_translate("statistics_window", "Form"))
        self.filmDirectors_label.setText(_translate("statistics_window", "Film directors:"))
        self.movies_label.setText(_translate("statistics_window", "Movies:"))
        self.genres_label.setText(_translate("statistics_window", "Genres:"))
