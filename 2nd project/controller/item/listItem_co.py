from PyQt5 import QtWidgets
from ui.item.list_ui import Ui_Form
from controller.item.ajouterItem import AjouterItemDialog
from controller.item.modifierItem import ModifierItemDialog

class ListItem_Co(QtWidgets.QWidget):
    def __init__(self, parent):
        from controller.mainFrame_co import MainFrame_Co
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent:MainFrame_Co = parent

        self.buttonsBindings()

    def buttonsBindings(self):
        self.ui.ajouter_pushButton.clicked.connect(self.handleAjouter)
        self.ui.modifier_pushButton.clicked.connect(self.handleModifier)

    def handleAjouter(self):
        ajouterItemDialog = AjouterItemDialog(self)
        ajouterItemDialog.exec_()
    
    def handleModifier(self):
        modifierItemDialog = ModifierItemDialog(self)
        modifierItemDialog.exec_()