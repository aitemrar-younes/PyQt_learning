from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from ui.transaction_ui.AddTransactionWidget_ui import Ui_Form
from model.item import Item

class AjouterTransactionWidget(QtWidgets.QWidget):
    def __init__(self, item) :
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.item_comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.item:Item = item

    def refresh(self):
        self.loadComboItem()

    def loadComboItem(self):
        self.ui.item_comboBox.clear()
        data = self.item.list_item_all()
        for item in data:
            #print(item)
            self.ui.item_comboBox.addItem(item['nom'])