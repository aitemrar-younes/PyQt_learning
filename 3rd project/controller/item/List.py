from PyQt5 import QtWidgets
from ui.Item.List_ui import Ui_Form
from controller.item.Ajouter import ItemAjouter

class ItemList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.buttonsBindings()

    def buttonsBindings(self):
        self.ui.ajouter_pushButton.clicked.connect(self.AjouterClicked)

    def AjouterClicked(self):
        dialog = ItemAjouter()
        dialog.exec_()