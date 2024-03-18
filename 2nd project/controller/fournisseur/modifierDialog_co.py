from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys
from ui.fournisseur_ui.ModifierDialog_ui import Ui_Dialog

class ModifierDialog_Co(QDialog):
    def __init__(self, fournisseur_id, parent=None):
        from controller.fournisseur.listFournisseur_co import ListFournisseur_Co
        super(ModifierDialog_Co, self).__init__(parent)
        self.fournisseur_id = fournisseur_id
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent:ListFournisseur_Co = parent

        self.buttonsBindings()
        self.loadFields()

    def buttonsBindings(self):
        self.ui.modifier_pushButton.clicked.connect(self.handleModifier)
        self.ui.annuler_pushButton.clicked.connect(self.close)

    def loadFields(self):
        self.data = self.parent.parent.fournisseur.getById(id=self.fournisseur_id)
        
        self.ui.lineEdit.setText(self.data['nom'])
        self.ui.prenom_lineEdit.setText(self.data['prenom'])
        self.ui.num_lineEdit.setText(self.data['num'])

    def handleModifier(self):
        self.accept()
