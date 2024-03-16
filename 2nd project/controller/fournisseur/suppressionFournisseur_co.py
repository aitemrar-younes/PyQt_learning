from PyQt5 import QtWidgets
from ui.fournisseur_ui.SuppressionFournisseurConfirmation_ui import Ui_Dialog

class SuppressionFournisseur_Co(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)