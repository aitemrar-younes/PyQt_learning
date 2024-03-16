import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from controller.mainFrame_co import MainFrame_Co
from model.db import DB

class MyDialog(QMessageBox):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.setWindowTitle("Error")
        self.setText("Failed to connect to the database.")
        self.setIcon(QMessageBox.Critical)
        self.addButton(QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication([])
    db = DB()
    response = db.connect()
    #print(response)

    if db.connection is None:
        dialog = MyDialog()
        dialog.exec_()
        sys.exit()
        
    window = MainFrame_Co(db)
    window.show()
    sys.exit(app.exec_())