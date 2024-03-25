from PyQt5 import QtWidgets
from ui.Fournisseur.Ajouter_ui import Ui_Dialog

class PoleList(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)