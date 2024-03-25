from PyQt5 import QtWidgets
import sys
from ui.mainWindow_ui import Ui_MainWindow

from controller.fournisseur.List import FournisseurList
from controller.item.List import ItemList
from controller.pole.List import PoleList
from controller.nt.List import NTList

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        fournisseurList = FournisseurList()
        itemList = ItemList()
        poleList = PoleList()
        nTList = NTList()

        self.ui.stackedWidget.addWidget(fournisseurList)
        self.ui.stackedWidget.addWidget(itemList)
        self.ui.stackedWidget.addWidget(poleList)
        self.ui.stackedWidget.addWidget(nTList)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.buttonsBindings()


    def buttonsBindings(self):
        self.ui.fournisseur_pushButton.clicked.connect(lambda: self.switchTo(0))
        self.ui.item_pushButton.clicked.connect(lambda: self.switchTo(1))
        self.ui.pole_pushButton.clicked.connect(lambda: self.switchTo(2))
        self.ui.nt_pushButton.clicked.connect(lambda: self.switchTo(3))

        self.ui.deconnexion_pushButton.clicked.connect(lambda: sys.exit())

    def switchTo(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)