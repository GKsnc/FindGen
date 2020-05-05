'''
@author Ryder
@create 2020-03-24-20:45
'''
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget


from DeliveryUI.form3 import Ui_Form3


class ThreePanel(QWidget, Ui_Form3):
    def __init__(self, parent=None):
        super(ThreePanel, self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_pushButton_chooseimg_clicked(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        self.label.setPixmap(QtGui.QPixmap(fname))
        self.label.setScaledContents(True)
    @pyqtSlot()
    def on_pushButton_reasonsubmit_clicked(self):
        reason = self.textEdit_reason.toPlainText()  #reason就是得到的页面上输入的理由
        dialog = QtWidgets.QDialog()
        dialog.resize(300, 200)
        button = QtWidgets.QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(110, 150)
        dialog.setWindowTitle('提交信息')
        labelText1 = QtWidgets.QLabel('提交成功', dialog)
        labelText1.move(110, 70)
        dialog.exec()


