from PyQt5 import QtWidgets
from ui.addWidget_ui import Ui_addWidget
from model.fournisseur import Fournisseur

class AjouterFournisseurWidget(QtWidgets.QWidget):
    def __init__(self, fournisseur):
        super().__init__()
        self.ui = Ui_addWidget()
        self.ui.setupUi(self)
        self.fournisseur:Fournisseur = fournisseur

        #Binding buttons clicks
        self.ui.ajouter_pushButton.clicked.connect(self.ajouterFournisseur)

    def refresh(self):
        self.clearFields()

    def clearFields(self):
        self.ui.nomFournisseur_lineEdit.setText('')
        self.ui.prenomFournisseur_lineEdit.setText('')
        self.ui.numFournisseur_lineEdit.setText('')
        self.ui.addressFournisseur_lineEdit.setText('')


    def ajouterFournisseur(self):
        nom = self.ui.nomFournisseur_lineEdit.text()
        prenom = self.ui.prenomFournisseur_lineEdit.text()
        num = self.ui.numFournisseur_lineEdit.text()
        address = self.ui.addressFournisseur_lineEdit.text()
        data = ( nom, prenom, num, address, )
        self.fournisseur.ajouter_fournisseur(data)