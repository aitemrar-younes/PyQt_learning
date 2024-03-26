from PyQt5 import QtWidgets
from ui.Nt.List_ui import Ui_Form
from controller.nt.Ajouter import NTAjouter

class NTList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.buttonsBindings()

    def buttonsBindings(self):
        self.ui.ajouter_pushButton.clicked.connect(self.AjouterClicked)

    def AjouterClicked(self):
        dialog = NTAjouter()
        dialog.exec_()