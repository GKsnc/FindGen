'''
@author Ryder
@create 2020-03-24-17:12
'''
import sys
import os
import time
import datetime
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5 import QtWidgets,QtGui,QtCore
from DeliveryUI.Login import Ui_Dialog
from DeliveryUI.Option import Ui_MainWindow
from DeliveryUI.register import Ui_Dialog_register
from DeliveryUI.One_Panel import OnePanel
from DeliveryUI.Three_Panel import ThreePanel
from DeliveryUI.Two_Panel import TwoPanel
from DeliveryUI.Four_Panel import FourPanel

from PyQt5.QtCore import pyqtSlot
import sqlite3


class Ui_Dialog_register(QWidget,Ui_Dialog_register):
    def __init__(self, parent = None):
        super(Ui_Dialog_register, self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_pushButton_register_clicked(self):
        conn = sqlite3.connect('.\Delivery.db')
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        cuisor = conn.cursor()
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        if account and password:
            cuisor.execute("INSERT INTO user(account, password, datestamp) VALUES (?, ?, ?)",
                      (account, password, date))
            conn.commit()
        cuisor.close()
        conn.close()

class Ui_Login_Dialog(QWidget, Ui_Dialog):
    def __init__(self, parent = None):
        super(Ui_Login_Dialog, self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_pushButton_login_clicked(self):
        self.ShowLoginResult()
    def ShowLoginResult(self):
        self.UserName = '?'
        self.Password = '?'
        conn = sqlite3.connect('.\Delivery.db')
        cuisor = conn.cursor()
        cuisor.execute("select * from user where account = '%s'" % self.lineEdit_login_UserName.text())
        # if cuisor.fetchall() == '':
        #     print(1111)
        for row in cuisor.fetchall():
            self.UserName = row[1]
            self.Password = row[2]
        # print(len(cuisor.fetchall()))
        # if not (len(cuisor.fetchall()) > 0):
        #     print(111)
        #     for row in cuisor.fetchall():
        #         self.UserName = row[1]
        #         self.Password = row[2]

        if (self.lineEdit_login_UserName.text() == self.UserName and self.lineEdit_login_Password.text() == self.Password):
            login_result = 'Login successfully'
            self.LoginDialog.close()




        else:
            dialog = QtWidgets.QDialog()
            dialog.resize(300, 200)
            button = QtWidgets.QPushButton('确定', dialog)
            button.clicked.connect(dialog.close)
            button.move(110, 150)
            dialog.setWindowTitle('登陆信息')
            if (self.lineEdit_login_UserName.text() == self.UserName and self.lineEdit_login_Password.text() != self.Password):

                login_result = 'Password error'
                labelText2 = QtWidgets.QLabel('密码错误', dialog)
                labelText2.move(110, 70)
                dialog.exec()
            else:
                login_result = 'UserName error'
                labelText3 = QtWidgets.QLabel('账号错误', dialog)
                labelText3.move(110, 70)
                dialog.exec()
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        login_name = self.lineEdit_login_UserName.text()
        cuisor.execute("insert into login_info(account, datestamp, login_result) values (?, ?, ?)",
                       (login_name, date, login_result))
        conn.commit()
        cuisor.close()
        conn.close()


class Main(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.qsl = QStackedLayout(self.frame)
        stack1 = OnePanel()
        stack2 = TwoPanel()
        stack3 = ThreePanel()
        stack4 = FourPanel()
        self.qsl.addWidget(stack1)
        self.qsl.addWidget(stack2)
        self.qsl.addWidget(stack3)
        self.qsl.addWidget(stack4)



    @pyqtSlot()
    def on_pushButton_gotologin_clicked(self):
        self.Win = Ui_Login_Dialog()
        self.setWindowTitle("用户登录")
        self.Win.show()
        self.toolButton_usename_4.setEnabled(True)
        self.toolButton_usename_2.setEnabled(True)
        self.toolButton_usename_3.setEnabled(True)
        self.toolButton_usename.setEnabled(True)
        self.frame.setEnabled(True)
        self.label_showoption.setEnabled(True)
    @pyqtSlot()
    def on_pushButton_gotoregister_clicked(self):
        self.Win = Ui_Dialog_register()
        self.Win.show()
    @pyqtSlot()
    def on_toolButton_usename_clicked(self):
        self.qsl.setCurrentIndex(0)
        self.label_showoption.setText("账户信息")
        self.label.setVisible(True)
        self.label_uername.setVisible(True)

    @pyqtSlot()
    def on_toolButton_usename_2_clicked(self):
        self.qsl.setCurrentIndex(1)
        self.label_showoption.setText("查询物流")
    @pyqtSlot()
    def on_toolButton_usename_4_clicked(self):
        self.qsl.setCurrentIndex(2)
        self.label_showoption.setText("虚假举报")
    @pyqtSlot()
    def on_toolButton_usename_3_clicked(self):
        self.qsl.setCurrentIndex(3)
        self.label_showoption.setText("问题反馈")




#
#


def main():
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    os._exit(app.exec_())

if __name__ == '__main__':
    main()
