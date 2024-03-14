from ui.Item_ui.AddItemWidget_ui import Ui_addItem_Form
from PyQt5 import QtWidgets
from model.item import Item


class AjouterItemWidget(QtWidgets.QWidget):
    def __init__(self, parent, item):
        from controller.mainFrameQMainWindow import MainFrameQMainWindow
        super().__init__()
        self.ui = Ui_addItem_Form()
        self.ui.setupUi(self)
        self.item:Item = item
        self.parent:MainFrameQMainWindow = parent

        # inner calls
        self.buttons_bind()

    def refresh(self):
        self.clearFields()

    def clearFields(self):
        self.ui.nom_lineEdit.setText('')
        self.ui.designation_lineEdit.setText('')

    def buttons_bind(self):
        self.ui.save_pushButton.clicked.connect(self.ajouterItem)

    def ajouterItem(self):
        data = self.valider_data()
        if data == None:
            return
        
        response = self.item.ajouter_item(data)
        if response['is_ok']:
            self.parent.ui.stackedWidget.setCurrentIndex(0) # a changer aprés a l'index de la liste des items
        else:
            QtWidgets.QMessageBox.critical(None, "Insertion Echoué", response['message'])

    def valider_data(self):
        nom = self.ui.nom_lineEdit.text().upper().strip()
        designation = self.ui.designation_lineEdit.text()
        if nom == '':
            QtWidgets.QMessageBox.critical(None, "Information Invalid", "Veuillez sisir le nom de l'item")
            return None
        data = ( nom, designation, )
        return data
