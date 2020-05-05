# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_register(object):
    def setupUi(self, Dialog_register):
        Dialog_register.setObjectName("Dialog_register")
        Dialog_register.resize(411, 462)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog_register)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 130, 201, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_register = QtWidgets.QPushButton(Dialog_register)
        self.pushButton_register.setGeometry(QtCore.QRect(110, 260, 93, 28))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_register)
        self.pushButton_cancel.setGeometry(QtCore.QRect(220, 260, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Dialog_register)
        QtCore.QMetaObject.connectSlotsByName(Dialog_register)

    def retranslateUi(self, Dialog_register):
        _translate = QtCore.QCoreApplication.translate
        Dialog_register.setWindowTitle(_translate("Dialog_register", "Dialog"))
        self.label.setText(_translate("Dialog_register", "账户"))
        self.label_2.setText(_translate("Dialog_register", "密码"))
        self.pushButton_register.setText(_translate("Dialog_register", "注册"))
        self.pushButton_cancel.setText(_translate("Dialog_register", "取消"))

