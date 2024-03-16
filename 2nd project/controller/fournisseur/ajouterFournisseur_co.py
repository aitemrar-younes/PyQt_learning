from PyQt5 import QtWidgets
from ui.fournisseur_ui.AjouterFournisseur_ui import Ui_Form

class AjouterFournisseur_Co(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        from controller.mainFrame_co import MainFrame_Co
        self.parent:MainFrame_Co = parent
        self.buttonBindings()

    def load(self):
        self.clearFields()

    def buttonBindings(self):
        self.ui.annuler_pushButton.clicked.connect(lambda : self.parent.swithToPage(0))
        self.ui.ajouter_pushButton.clicked.connect(lambda : self.handleAjouter())
        self.ui.ajouterPlus_pushButton.clicked.connect(lambda : self.handleAjouter(more=True))

    def handleAjouter(self, more=False):
        data = self.valider()
        if data:
            response = self.parent.fournisseur.inserer(data)
            if response['is_ok']:
                if more:
                    self.clearFields()
                else:
                    self.parent.swithToPage(0)


    def valider(self):
        nom = self.ui.nom_lineEdit.text().strip().upper()
        prenom = self.ui.prenom_lineEdit.text().strip().capitalize()
        num = self.ui.num_lineEdit.text().strip().upper()
        status = self.ui.status_checkBox.isChecked()

        if not (nom and prenom):
            QtWidgets.QMessageBox.critical(None, "Informations invalid", "Veuillez saisir le nom et le prenom")
            return None
        return ( nom, prenom, num )

    def clearFields(self):
        self.ui.nom_lineEdit.setText('')
        self.ui.prenom_lineEdit.setText('')
        self.ui.num_lineEdit.setText('')
        self.ui.status_checkBox.setChecked(False)