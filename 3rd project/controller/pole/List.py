from PyQt5 import QtWidgets
from ui.Pole.List_ui import Ui_Form

class PoleList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)