from PyQt5 import QtWidgets
import sys
from ui.mainWindow_ui import Ui_MainWindow

from controller.dashboard.List import DashBoardList
from controller.fournisseur.List import FournisseurList
from controller.item.List import ItemList
from controller.pole.List import PoleList
from controller.nt.List import NTList

from controller.chauffeur.List import ChauffeurList
from controller.voiture.List import VoitureList

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        dashBoardList = DashBoardList()
        fournisseurList = FournisseurList()
        itemList = ItemList()
        poleList = PoleList()
        nTList = NTList()

        chauffeurList = ChauffeurList()
        voitureList = VoitureList()

        self.ui.stackedWidget.addWidget(dashBoardList)
        self.ui.stackedWidget.addWidget(fournisseurList)
        self.ui.stackedWidget.addWidget(itemList)
        self.ui.stackedWidget.addWidget(poleList)
        self.ui.stackedWidget.addWidget(nTList)

        self.ui.stackedWidget.addWidget(chauffeurList)
        self.ui.stackedWidget.addWidget(voitureList)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.buttonsBindings()


    def buttonsBindings(self):
        self.ui.dashBoard_pushButton.clicked.connect(lambda: self.switchTo(0))
        self.ui.fournisseur_pushButton.clicked.connect(lambda: self.switchTo(1))
        self.ui.item_pushButton.clicked.connect(lambda: self.switchTo(2))
        self.ui.pole_pushButton.clicked.connect(lambda: self.switchTo(3))
        self.ui.nt_pushButton.clicked.connect(lambda: self.switchTo(4))

        self.ui.chauffeur_pushButton.clicked.connect(lambda: self.switchTo(5))
        self.ui.voiture_pushButton.clicked.connect(lambda: self.switchTo(6))

        self.ui.deconnexion_pushButton.clicked.connect(lambda: sys.exit())

    def switchTo(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)