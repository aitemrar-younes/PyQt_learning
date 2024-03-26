from PyQt5 import QtWidgets
from ui.Pole.List_ui import Ui_Form
from controller.pole.Ajouter import PoleAjouter

class PoleList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.buttonsBindings()

    def buttonsBindings(self):
        self.ui.ajouter_pushButton.clicked.connect(self.AjouterClicked)

    def AjouterClicked(self):
        dialog = PoleAjouter()
        dialog.exec_()