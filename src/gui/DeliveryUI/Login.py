# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 531)
        self.LoginDialog = Dialog
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(430, 100, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_img = QtWidgets.QLabel(Dialog)
        self.label_img.setGeometry(QtCore.QRect(80, 140, 181, 221))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap(":/image/health.png"))
        self.label_img.setObjectName("label_img")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(430, 189, 241, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_login_UserName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_login_UserName.setText("")
        self.lineEdit_login_UserName.setObjectName("lineEdit_login_UserName")
        self.gridLayout.addWidget(self.lineEdit_login_UserName, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_login_Password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_login_Password.setText("")
        self.lineEdit_login_Password.setObjectName("lineEdit_login_Password")
        self.gridLayout.addWidget(self.lineEdit_login_Password, 1, 1, 1, 1)
        self.pushButton_gotoregister = QtWidgets.QPushButton(Dialog)
        self.pushButton_gotoregister.setGeometry(QtCore.QRect(560, 340, 93, 28))
        self.pushButton_gotoregister.setObjectName("pushButton_gotoregister")
        self.pushButton_login = QtWidgets.QPushButton(Dialog)
        self.pushButton_login.setGeometry(QtCore.QRect(440, 340, 93, 28))
        self.pushButton_login.setObjectName("pushButton_login")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Welcome"))
        self.label.setText(_translate("Dialog", "账号"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.pushButton_gotoregister.setText(_translate("Dialog", "注册"))
        self.pushButton_login.setText(_translate("Dialog", "登陆"))

import agv_icon_rc
