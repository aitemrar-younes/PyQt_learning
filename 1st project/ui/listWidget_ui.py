# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listWidget(object):
    def setupUi(self, listWidget):
        listWidget.setObjectName("listWidget")
        listWidget.resize(955, 595)
        self.gridLayout = QtWidgets.QGridLayout(listWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(listWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 27))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(listWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pageSize_comboBox = QtWidgets.QComboBox(listWidget)
        self.pageSize_comboBox.setMinimumSize(QtCore.QSize(60, 27))
        self.pageSize_comboBox.setEditable(False)
        self.pageSize_comboBox.setObjectName("pageSize_comboBox")
        self.pageSize_comboBox.addItem("")
        self.pageSize_comboBox.addItem("")
        self.pageSize_comboBox.addItem("")
        self.pageSize_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.pageSize_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.chercherFournisseur_lineEdit = QtWidgets.QLineEdit(listWidget)
        self.chercherFournisseur_lineEdit.setMinimumSize(QtCore.QSize(0, 27))
        self.chercherFournisseur_lineEdit.setObjectName("chercherFournisseur_lineEdit")
        self.horizontalLayout.addWidget(self.chercherFournisseur_lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ajouterFournisseur_pushButton = QtWidgets.QPushButton(listWidget)
        self.ajouterFournisseur_pushButton.setMinimumSize(QtCore.QSize(0, 27))
        self.ajouterFournisseur_pushButton.setObjectName("ajouterFournisseur_pushButton")
        self.horizontalLayout.addWidget(self.ajouterFournisseur_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.fournisseurList_tableWidget = QtWidgets.QTableWidget(listWidget)
        self.fournisseurList_tableWidget.setEnabled(True)
        self.fournisseurList_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fournisseurList_tableWidget.setObjectName("fournisseurList_tableWidget")
        self.fournisseurList_tableWidget.setColumnCount(5)
        self.fournisseurList_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseurList_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseurList_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseurList_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseurList_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseurList_tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.fournisseurList_tableWidget, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.supprimerFournisseur_pushButton = QtWidgets.QPushButton(listWidget)
        self.supprimerFournisseur_pushButton.setMinimumSize(QtCore.QSize(0, 27))
        self.supprimerFournisseur_pushButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.supprimerFournisseur_pushButton.setObjectName("supprimerFournisseur_pushButton")
        self.horizontalLayout_2.addWidget(self.supprimerFournisseur_pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.modifierFournisseur_pushButton = QtWidgets.QPushButton(listWidget)
        self.modifierFournisseur_pushButton.setMinimumSize(QtCore.QSize(0, 27))
        self.modifierFournisseur_pushButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.modifierFournisseur_pushButton.setObjectName("modifierFournisseur_pushButton")
        self.horizontalLayout_2.addWidget(self.modifierFournisseur_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(listWidget)
        QtCore.QMetaObject.connectSlotsByName(listWidget)

    def retranslateUi(self, listWidget):
        _translate = QtCore.QCoreApplication.translate
        listWidget.setWindowTitle(_translate("listWidget", "Form"))
        self.label.setText(_translate("listWidget", "List fournisseur"))
        self.label_2.setText(_translate("listWidget", "Afficher par"))
        self.pageSize_comboBox.setCurrentText(_translate("listWidget", "10"))
        self.pageSize_comboBox.setItemText(0, _translate("listWidget", "10"))
        self.pageSize_comboBox.setItemText(1, _translate("listWidget", "25"))
        self.pageSize_comboBox.setItemText(2, _translate("listWidget", "50"))
        self.pageSize_comboBox.setItemText(3, _translate("listWidget", "All"))
        self.chercherFournisseur_lineEdit.setPlaceholderText(_translate("listWidget", "Chercher"))
        self.ajouterFournisseur_pushButton.setText(_translate("listWidget", "Ajouter"))
        self.fournisseurList_tableWidget.setSortingEnabled(True)
        item = self.fournisseurList_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("listWidget", "ID"))
        item = self.fournisseurList_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("listWidget", "Nom"))
        item = self.fournisseurList_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("listWidget", "Prenom"))
        item = self.fournisseurList_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("listWidget", "Num"))
        item = self.fournisseurList_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("listWidget", "Address"))
        self.supprimerFournisseur_pushButton.setText(_translate("listWidget", "Supprimer"))
        self.modifierFournisseur_pushButton.setText(_translate("listWidget", "Modifier"))
