# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form4(object):
    def setupUi(self, Form4):
        Form4.setObjectName("Form4")
        Form4.resize(472, 367)
        self.textEdit_problem = QtWidgets.QTextEdit(Form4)
        self.textEdit_problem.setGeometry(QtCore.QRect(60, 60, 291, 131))
        self.textEdit_problem.setObjectName("textEdit_problem")
        self.pushButton_problemsubmit = QtWidgets.QPushButton(Form4)
        self.pushButton_problemsubmit.setGeometry(QtCore.QRect(60, 230, 93, 28))
        self.pushButton_problemsubmit.setObjectName("pushButton_problemsubmit")

        self.retranslateUi(Form4)
        QtCore.QMetaObject.connectSlotsByName(Form4)

    def retranslateUi(self, Form4):
        _translate = QtCore.QCoreApplication.translate
        Form4.setWindowTitle(_translate("Form4", "Form"))
        self.pushButton_problemsubmit.setText(_translate("Form4", "提交"))

