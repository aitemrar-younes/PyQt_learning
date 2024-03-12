from PyQt5 import QtWidgets
from ui.listWidget_ui import Ui_listWidget
from model.fournisseur import Fournisseur

class ListFournisseurWidget(QtWidgets.QWidget):
    def __init__(self, fournisseur):
        super().__init__()
        self.ui = Ui_listWidget()
        self.ui.setupUi(self)
        self.fournisseur:Fournisseur = fournisseur
        self.fillTable()
        self.ui.pageSize_comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        #params
        self.ui.fournisseurList_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.fournisseurList_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        #Bindibgs buttons
        self.ui.supprimerFournisseur_pushButton.clicked.connect(self.getSelectedRows)
    
    def refresh(self):
        self.fillTable()
    
    def fillTable(self):
        data = self.fournisseur.list_fournisseur_all()
        self.ui.fournisseurList_tableWidget.setRowCount(len(data))

        for row, rowData in enumerate(data):
            for col, value in enumerate(rowData):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.ui.fournisseurList_tableWidget.setItem(row, col, item)
        # Resize columns to contents
        self.ui.fournisseurList_tableWidget.resizeColumnsToContents()
        last_col_index = self.ui.fournisseurList_tableWidget.columnCount()-1
        self.ui.fournisseurList_tableWidget.horizontalHeader().setSectionResizeMode(last_col_index, QtWidgets.QHeaderView.Stretch)
        self.ui.fournisseurList_tableWidget.verticalHeader().setVisible(False)

    def getSelectedRows(self):
        selected_rows = set()

        for item in self.ui.fournisseurList_tableWidget.selectedItems():
            selected_rows.add(item.row())
            #print(se)

        print(f"Selected Rows: {list(selected_rows)}")
        self.ui.fournisseurList_tableWidget.clearSelection()

