from PyQt5 import QtWidgets
from ui.Fournisseur.List_ui import Ui_Form
from controller.fournisseur.Ajouter import FournisseurAjouter

class FournisseurList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.buttonsBindings()

    def buttonsBindings(self):
        self.ui.ajouter_pushButton.clicked.connect(self.AjouterClicked)

    def AjouterClicked(self):
        dialog = FournisseurAjouter()
        dialog.exec_()