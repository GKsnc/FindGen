'''
@author Ryder
@create 2020-03-24-20:45
'''
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from DeliveryUI.form2 import Ui_Form2


class TwoPanel(QWidget, Ui_Form2):
    def __init__(self, parent=None):
        super(TwoPanel, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_query_clicked(self):
        delivery_number = self.lineEdit_deliverynumber.text()#这里快递单号判断，然后返回结果
        self.textBrowser_deliveryresult.setText("此快递正在派送中，预计今日送达")
