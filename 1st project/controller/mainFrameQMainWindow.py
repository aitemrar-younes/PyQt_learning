import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5 import QtWidgets

from ui.mainFrame_ui import Ui_MainWindow
from controller.listFournisseurWidget import ListFournisseurWidget
from controller.ajouterFournisseurWidget import AjouterFournisseurWidget
from controller.aboutWidget import AboutWidget
from controller.ajouterItemWidget import AjouterItemWidget
from controller.ajouterTransactionWidget import AjouterTransactionWidget

from model.db import DB
from model.fournisseur import Fournisseur

class MainFrameQMainWindow(QtWidgets.QMainWindow):
    def __init__(self, fournisseur, item):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fournisseur = fournisseur
        self.item = item

        # Linking the widget's pages
        self.listFournisseurWidget = ListFournisseurWidget(fournisseur)
        self.ui.stackedWidget.addWidget(self.listFournisseurWidget)
        self.ajouterFournisseurWidget = AjouterFournisseurWidget(fournisseur)
        self.ui.stackedWidget.addWidget(self.ajouterFournisseurWidget)
        self.aboutWidget = AboutWidget()
        self.ui.stackedWidget.addWidget(self.aboutWidget)
        self.ajouterItemWidget = AjouterItemWidget(item, self)
        self.ui.stackedWidget.addWidget(self.ajouterItemWidget)
        self.ajouterTransactionWidget = AjouterTransactionWidget()
        self.ui.stackedWidget.addWidget(self.ajouterTransactionWidget)
        self.ui.stackedWidget.setCurrentIndex(0)

        # binding buttons click
        self.ui.actionList.triggered.connect(lambda:self.switch_to(0))
        self.ui.actionAjouter.triggered.connect(lambda:self.switch_to(1))
        self.ui.actionAbout.triggered.connect(lambda:self.switch_to(2))
        self.ui.itemList_action.triggered.connect(lambda:self.switch_to(3))
        self.ui.ajouterTransactions_action.triggered.connect(lambda:self.switch_to(4))

        #
        self.listFournisseurWidget.ui.ajouterFournisseur_pushButton.clicked.connect(lambda:self.switch_to(1))
        self.ajouterFournisseurWidget.ui.annulerAjouter_pushButton.clicked.connect(lambda:self.switch_to(0))

    def switch_to(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        if index == 0:
            self.listFournisseurWidget.refresh()
        if index == 1:
            self.ajouterFournisseurWidget.refresh()
        if index == 3:
            self.ajouterItemWidget.refresh()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    db = DB()
    fournisseur = Fournisseur(db)
    main_window = MainFrameQMainWindow(fournisseur)
    main_window.show()
    sys.exit(app.exec_())