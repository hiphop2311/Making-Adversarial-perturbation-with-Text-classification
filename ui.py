# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyApp(object):
    def setupUi(self, MyApp):
        MyApp.setObjectName("MyApp")
        MyApp.resize(831, 314)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(MyApp)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 80, 381, 191))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.line = QtWidgets.QFrame(MyApp)
        self.line.setGeometry(QtCore.QRect(410, 80, 16, 191))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.linePath = QtWidgets.QLineEdit(MyApp)
        self.linePath.setGeometry(QtCore.QRect(90, 20, 251, 21))
        self.linePath.setObjectName("linePath")
        self.selectFileButton = QtWidgets.QPushButton(MyApp)
        self.selectFileButton.setGeometry(QtCore.QRect(340, 15, 61, 31))
        self.selectFileButton.setObjectName("selectFileButton")
        self.perturbTextButton = QtWidgets.QPushButton(MyApp)
        self.perturbTextButton.setGeometry(QtCore.QRect(420, 15, 161, 31))
        self.perturbTextButton.setObjectName("perturbTextButton")
        self.label_2 = QtWidgets.QLabel(MyApp)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MyApp)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 151, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(MyApp)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 151, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(MyApp)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(430, 80, 381, 191))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_predict_2 = QtWidgets.QLabel(MyApp)
        self.label_predict_2.setGeometry(QtCore.QRect(540, 280, 191, 16))
        self.label_predict_2.setText("")
        self.label_predict_2.setObjectName("label_predict_2")
        self.label_7 = QtWidgets.QLabel(MyApp)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 151, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(MyApp)
        self.label_8.setGeometry(QtCore.QRect(430, 60, 151, 16))
        self.label_8.setObjectName("label_8")
        self.predictButton_1 = QtWidgets.QPushButton(MyApp)
        self.predictButton_1.setGeometry(QtCore.QRect(15, 275, 113, 32))
        self.predictButton_1.setObjectName("predictButton_1")
        self.predictButton_2 = QtWidgets.QPushButton(MyApp)
        self.predictButton_2.setGeometry(QtCore.QRect(425, 275, 113, 32))
        self.predictButton_2.setObjectName("predictButton_2")
        self.label_predict_1 = QtWidgets.QLabel(MyApp)
        self.label_predict_1.setGeometry(QtCore.QRect(140, 280, 191, 16))
        self.label_predict_1.setText("")
        self.label_predict_1.setObjectName("label_predict_1")

        self.retranslateUi(MyApp)
        QtCore.QMetaObject.connectSlotsByName(MyApp)

    def retranslateUi(self, MyApp):
        _translate = QtCore.QCoreApplication.translate
        MyApp.setWindowTitle(_translate("MyApp", "Form"))
        self.selectFileButton.setText(_translate("MyApp", "..."))
        self.perturbTextButton.setText(_translate("MyApp", "Make perturbations"))
        self.label_2.setText(_translate("MyApp", "Select file:"))
        self.label_7.setText(_translate("MyApp", "Raw data:"))
        self.label_8.setText(_translate("MyApp", "Perturbed data:"))
        self.predictButton_1.setText(_translate("MyApp", "Predict"))
        self.predictButton_2.setText(_translate("MyApp", "Predict"))
