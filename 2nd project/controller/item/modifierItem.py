from PyQt5 import QtWidgets
from ui.item.modifier_ui import Ui_Dialog

class ModifierItemDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        from controller.item.listItem_co import ListItem_Co
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent:ListItem_Co = parent

        self.buttonsBindings()

    def buttonsBindings(self):
        self.ui.modifier_pushButton.clicked.connect(self.accept)
        self.ui.annuler_pushButton.clicked.connect(self.close)