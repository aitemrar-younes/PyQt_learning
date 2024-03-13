from ui.Item_ui.AddItemWidget_ui import Ui_addItem_Form
from PyQt5 import QtWidgets

class AjouterItemWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_addItem_Form()
        self.ui.setupUi(self)
