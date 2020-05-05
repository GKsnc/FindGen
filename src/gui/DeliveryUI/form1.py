# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(436, 329)
        self.gridLayoutWidget = QtWidgets.QWidget(Form1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 110, 271, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_uername = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_uername.setText("")
        self.label_uername.setObjectName("label_uername")
        self.gridLayout.addWidget(self.label_uername, 0, 1, 1, 1)

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "Form"))
        self.label.setText(_translate("Form1", "账户"))

