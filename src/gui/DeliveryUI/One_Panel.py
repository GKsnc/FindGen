'''
@author Ryder
@create 2020-03-24-20:45
'''
from PyQt5.QtWidgets import QWidget

from DeliveryUI.form1 import Ui_Form1


class OnePanel(QWidget, Ui_Form1):
    def __init__(self, parent=None):
        super(OnePanel, self).__init__(parent)
        self.setupUi(self)
        self.label_uername.setText("admin")
        self.label.setVisible(False)
        self.label_uername.setVisible(False)