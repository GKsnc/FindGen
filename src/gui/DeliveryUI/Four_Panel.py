'''
@author Ryder
@create 2020-03-24-20:45
'''
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from form4 import Ui_Form4


class FourPanel(QWidget, Ui_Form4):
    def __init__(self, parent=None):
        super(FourPanel, self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_pushButton_problemsubmit_clicked(self):
        problem = self.textEdit_problem.toPlainText()
        dialog = QtWidgets.QDialog()
        dialog.resize(300, 200)
        button = QtWidgets.QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(110, 150)
        dialog.setWindowTitle('问题反馈')
        labelText1 = QtWidgets.QLabel('提交成功', dialog)
        labelText1.move(110, 70)
        dialog.exec()