# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(470, 377)
        self.label_3 = QtWidgets.QLabel(Form3)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form3)
        self.label.setGeometry(QtCore.QRect(130, 20, 131, 131))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_chooseimg = QtWidgets.QPushButton(Form3)
        self.pushButton_chooseimg.setGeometry(QtCore.QRect(310, 40, 93, 28))
        self.pushButton_chooseimg.setObjectName("pushButton_chooseimg")
        self.label_4 = QtWidgets.QLabel(Form3)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit_reason = QtWidgets.QTextEdit(Form3)
        self.textEdit_reason.setGeometry(QtCore.QRect(120, 180, 291, 131))
        self.textEdit_reason.setObjectName("textEdit_reason")
        self.pushButton_reasonsubmit = QtWidgets.QPushButton(Form3)
        self.pushButton_reasonsubmit.setGeometry(QtCore.QRect(120, 340, 93, 28))
        self.pushButton_reasonsubmit.setObjectName("pushButton_reasonsubmit")

        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Form"))
        self.label_3.setText(_translate("Form3", "上传图片"))
        self.label.setText(_translate("Form3", "图片"))
        self.pushButton_chooseimg.setText(_translate("Form3", "选择图片"))
        self.label_4.setText(_translate("Form3", "理由"))
        self.pushButton_reasonsubmit.setText(_translate("Form3", "提交"))

