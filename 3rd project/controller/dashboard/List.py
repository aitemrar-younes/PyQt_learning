from PyQt5 import QtWidgets
from ui.dashboard.List_ui import Ui_Form

class DashBoardList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)