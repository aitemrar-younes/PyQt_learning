import sys
from PyQt5 import QtWidgets
from ui.login_ui import Ui_Dialog
from model.db import DB

class LoginDialog(QtWidgets.QDialog):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db:DB = db
        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        if self.db.connect(username, password): #later i will pass these 2 fields to connection
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid credentials")
    def closeEvent(self, event):
        sys.exit()