# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(443, 378)
        self.label = QtWidgets.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(71, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_deliverynumber = QtWidgets.QLineEdit(Form2)
        self.lineEdit_deliverynumber.setGeometry(QtCore.QRect(120, 40, 141, 31))
        self.lineEdit_deliverynumber.setObjectName("lineEdit_deliverynumber")
        self.pushButton_query = QtWidgets.QPushButton(Form2)
        self.pushButton_query.setGeometry(QtCore.QRect(290, 40, 93, 28))
        self.pushButton_query.setObjectName("pushButton_query")
        self.textBrowser_deliveryresult = QtWidgets.QTextBrowser(Form2)
        self.textBrowser_deliveryresult.setGeometry(QtCore.QRect(70, 110, 331, 201))
        self.textBrowser_deliveryresult.setObjectName("textBrowser_deliveryresult")
        self.label_2 = QtWidgets.QLabel(Form2)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Form"))
        self.label.setText(_translate("Form2", "单号"))
        self.pushButton_query.setText(_translate("Form2", "查询"))
        self.label_2.setText(_translate("Form2", "结果"))

