import sys
from PyQt5 import QtWidgets
from model.db import DB
from model.fournisseur import Fournisseur
from model.item import Item
from controller.mainFrameQMainWindow import MainFrameQMainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    db = DB()
    fournisseur = Fournisseur(db)
    item = Item(db)
    main_window = MainFrameQMainWindow(fournisseur, item)
    main_window.show()
    sys.exit(app.exec_())