from PyQt5 import QtWidgets
from ui.item.list_ui import Ui_Form

class ListItem_Co(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent