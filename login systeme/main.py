from model.db import DB
import sys
from PyQt5 import QtWidgets
from controller.loginWidget import LoginDialog
from controller.mainFrameWidget import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    db = DB()
    login_dialog = LoginDialog(db)
    if login_dialog.exec_() == QtWidgets.QDialog.Accepted:
        main_window = MainWindow()
        main_window.setWindowTitle("Main Window")
        main_window.show()
        #login_dialog.close()
    sys.exit(app.exec_())