from PyQt5 import QtWidgets
from ui.Chauffeur.List_ui import Ui_Form

class ChauffeurList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)