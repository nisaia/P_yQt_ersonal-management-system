# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/demoScrollBar.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        self.horizontalScrollBarSugarLevel = QtWidgets.QScrollBar(Dialog)
        self.horizontalScrollBarSugarLevel.setGeometry(QtCore.QRect(220, 50, 300, 20))
        self.horizontalScrollBarSugarLevel.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarSugarLevel.setObjectName("horizontalScrollBarSugarLevel")
        self.horizontalSliderBloodPressure = QtWidgets.QSlider(Dialog)
        self.horizontalSliderBloodPressure.setGeometry(QtCore.QRect(220, 110, 300, 20))
        self.horizontalSliderBloodPressure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBloodPressure.setObjectName("horizontalSliderBloodPressure")
        self.verticalScrollBarPulseRate = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBarPulseRate.setGeometry(QtCore.QRect(180, 210, 20, 300))
        self.verticalScrollBarPulseRate.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarPulseRate.setObjectName("verticalScrollBarPulseRate")
        self.verticalSliderCholesterolLevel = QtWidgets.QSlider(Dialog)
        self.verticalSliderCholesterolLevel.setGeometry(QtCore.QRect(470, 220, 20, 300))
        self.verticalSliderCholesterolLevel.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderCholesterolLevel.setObjectName("verticalSliderCholesterolLevel")
        self.lineEditResult = QtWidgets.QLineEdit(Dialog)
        self.lineEditResult.setGeometry(QtCore.QRect(0, 550, 600, 26))
        self.lineEditResult.setObjectName("lineEditResult")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 121, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 161, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 111, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 210, 171, 18))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sugar level:"))
        self.label_2.setText(_translate("Dialog", "Blood pressure:"))
        self.label_3.setText(_translate("Dialog", "Pulse rate:"))
        self.label_4.setText(_translate("Dialog", "Cholesterol level:"))
