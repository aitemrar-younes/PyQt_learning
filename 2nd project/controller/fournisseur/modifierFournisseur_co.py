from PyQt5 import QtWidgets
from ui.fournisseur_ui.ModifierFournisseur_ui import Ui_Form

class ModifierFournisseur_Co(QtWidgets.QWidget):
    def __init__(self, parent):
        from controller.mainFrame_co import MainFrame_Co
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent:MainFrame_Co = parent
        self.buttonsBinding()
        
    def load(self):
        self.clearFields()
        self.loadFields()

    def buttonsBinding(self):
        self.ui.annuler_pushButton.clicked.connect(lambda : self.parent.swithToPage(0))
        self.ui.modifier_pushButton.clicked.connect(self.handleUpdate)

    def clearFields(self):
        self.ui.lineEdit.setText('')
        self.ui.prenom_lineEdit.setText('')
        self.ui.num_lineEdit.setText('')
        self.ui.status_checkBox.setChecked(False)

    def loadFields(self):
        fournisseur_tableWidget = self.parent.listFournisseur_Co.ui.fournisseur_tableWidget
        currentRow = fournisseur_tableWidget.currentRow()
        self.fournisseur_id = (fournisseur_tableWidget.item(currentRow, 0).text())
        self.data = self.parent.fournisseur.getById(id=self.fournisseur_id)
        
        self.ui.lineEdit.setText(self.data['nom'])
        self.ui.prenom_lineEdit.setText(self.data['prenom'])
        self.ui.num_lineEdit.setText(self.data['num'])

    def handleUpdate(self):
        data = self.valider()
        if data:
            response = self.parent.fournisseur.modifier(data)
            if response['is_ok']:
                self.clearFields()
                self.parent.swithToPage(0)


    def valider(self):
        nom = self.ui.lineEdit.text().strip().upper()
        prenom = self.ui.prenom_lineEdit.text().strip().capitalize()
        num = self.ui.num_lineEdit.text().strip().upper()
        status = self.ui.status_checkBox.isChecked()

        if not (nom and prenom):
            QtWidgets.QMessageBox.critical(None, "Informations invalid", "Veuillez saisir le nom et le prenom")
            return None
        return ( nom, prenom, num, self.fournisseur_id )