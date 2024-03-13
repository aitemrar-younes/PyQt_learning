from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from ui.transaction_ui.AddTransactionWidget_ui import Ui_Form

class AjouterTransactionWidget(QtWidgets.QWidget):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)