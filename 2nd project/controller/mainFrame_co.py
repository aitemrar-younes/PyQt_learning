from PyQt5 import QtWidgets

from model.db import DB
from model.fournisseur import Fournisseur
# UI Import
from ui.mainFrame_ui import Ui_MainWindow

# Pages controller Import
from controller.fournisseur.listFournisseur_co import ListFournisseur_Co
from controller.fournisseur.ajouterFournisseur_co import AjouterFournisseur_Co
from controller.fournisseur.modifierFournisseur_co import ModifierFournisseur_Co

class MainFrame_Co(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db:DB = db
        self.fournisseur = Fournisseur(self.db)

        # UI Instances
        self.listFournisseur_Co = ListFournisseur_Co(self)
        self.ajouterFournisseur_co = AjouterFournisseur_Co(self)
        self.modifierFournisseur_co = ModifierFournisseur_Co(self)

        self.ui.stackedWidget.addWidget(self.listFournisseur_Co)
        self.ui.stackedWidget.addWidget(self.ajouterFournisseur_co)
        self.ui.stackedWidget.addWidget(self.modifierFournisseur_co)

        self.ui.stackedWidget.setCurrentIndex(0)

        # 
        self.buttonsBindings()

    def buttonsBindings(self):
        # some binding should be in child where there is longer process
        self.ui.actionFournisseur.triggered.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))


    def swithToPage(self, index):
        self.ui.stackedWidget.widget(index).load()
        self.ui.stackedWidget.setCurrentIndex(index)