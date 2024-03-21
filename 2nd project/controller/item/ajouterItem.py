from PyQt5 import QtWidgets
from ui.item.ajouter_ui import Ui_Dialog

class AjouterItemDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent

        self.buttonsBindings()

    def buttonsBindings(self):
        self.ui.annuler_pushButton.clicked.connect(self.close)
        self.ui.ajouter_pushButton.clicked.connect(self.accept)
        self.ui.ajouterPlus_pushButton.clicked.connect(self.accept)

    def load(self):
        pass