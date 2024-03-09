from PyQt5 import QtWidgets
from ui.aboutWidget_ui import Ui_aboutWidget

class AboutWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_aboutWidget()
        self.ui.setupUi(self)