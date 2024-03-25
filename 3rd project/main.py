from PyQt5 import QtWidgets
from controller.mainWindow import MainWindow
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())