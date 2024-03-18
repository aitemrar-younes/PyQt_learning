from PyQt5 import QtWidgets 
import sys
from ui.fournisseur_ui.ModifierDialog_ui import Ui_Dialog
from ui.fournisseur_ui.ModifierFournisseur_ui import Ui_Form

class ModifierDialog_Co(QtWidgets.QDialog):
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
        self.ui.modifier_pushButton.clicked.connect(self.handleUpdate)
        self.ui.annuler_pushButton.clicked.connect(self.close)

    def loadFields(self):
        self.data = self.parent.parent.fournisseur.getById(id=self.fournisseur_id)
        
        self.ui.lineEdit.setText(self.data['nom'])
        self.ui.prenom_lineEdit.setText(self.data['prenom'])
        self.ui.num_lineEdit.setText(self.data['num'])

    def clearFields(self):
        self.ui.lineEdit.setText('')
        self.ui.prenom_lineEdit.setText('')
        self.ui.num_lineEdit.setText('')
        self.ui.status_checkBox.setChecked(False)

    def handleUpdate(self):
        data = self.valider()
        if data:
            response = self.parent.parent.fournisseur.modifier(data)
            if response['is_ok']:
                self.clearFields()
                self.parent.load()
                self.accept()
                #self.parent.parent.swithToPage(0)


    def valider(self):
        nom = self.ui.lineEdit.text().strip().upper()
        prenom = self.ui.prenom_lineEdit.text().strip().capitalize()
        num = self.ui.num_lineEdit.text().strip().upper()
        status = self.ui.status_checkBox.isChecked()

        if not (nom and prenom):
            QtWidgets.QMessageBox.critical(None, "Informations invalid", "Veuillez saisir le nom et le prenom")
            return None
        return ( nom, prenom, num, self.fournisseur_id )