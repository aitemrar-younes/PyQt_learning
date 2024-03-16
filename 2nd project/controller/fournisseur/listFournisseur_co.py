from PyQt5 import QtWidgets
from ui.fournisseur_ui.ListFournisseur_ui import Ui_FournisseurList
from controller.fournisseur.suppressionFournisseur_co import SuppressionFournisseur_Co

class ListFournisseur_Co(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_FournisseurList()
        self.ui.setupUi(self)
        self.styling()
        from controller.mainFrame_co import MainFrame_Co
        self.parent:MainFrame_Co = parent
        self.buttonsBindings()
        self.load()
        # QDialogue
        self.suppressionFournisseur_co = SuppressionFournisseur_Co()

    def load(self):
        self.loadTable()
        self.ui.fournisseur_tableWidget.clearSelection()

    def buttonsBindings(self):
        self.ui.ajouter_pushButton.clicked.connect(lambda : self.parent.swithToPage(1))
        self.ui.modifier_pushButton.clicked.connect(self.handleModifier)
        self.ui.supprimer_pushButton.clicked.connect(self.handleSuppressionConfirmation)

    def loadTable(self):
        data = self.parent.fournisseur.list()
        self.ui.fournisseur_tableWidget.setRowCount(len(data))
        for row_index, row in enumerate(data):
            for col_index, col in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(col))
                self.ui.fournisseur_tableWidget.setItem(row_index, col_index, item)

    
    def handleSuppressionConfirmation(self):
        if self.ui.fournisseur_tableWidget.selectionModel().hasSelection():
            currentRow = self.ui.fournisseur_tableWidget.currentRow()
            fournisseur_id = (self.ui.fournisseur_tableWidget.item(currentRow, 0).text())
            if  self.suppressionFournisseur_co.exec_() == QtWidgets.QDialog.Accepted:
                response = self.parent.fournisseur.supprimer(fournisseur_id)
                if not response['is_ok']:
                    QtWidgets.QMessageBox.critical(None, 'Erreur', 'Impossible de supprimer' )
                else:
                    self.load()
    def handleModifier(self):
        if self.ui.fournisseur_tableWidget.selectionModel().hasSelection():
            #self.currentRow = self.ui.fournisseur_tableWidget.currentRow()
            self.parent.swithToPage(2)

    def styling(self):
        self.ui.fournisseur_tableWidget.setStyleSheet(
            "QTableView::item:selected"
            "{"
            "background-color : #d9fffb;"
            "selection-color : #000000;"
            "}"
        )