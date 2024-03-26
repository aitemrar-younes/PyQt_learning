from PyQt5 import QtWidgets
from ui.Voiture.List_ui import Ui_Form

class VoitureList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)