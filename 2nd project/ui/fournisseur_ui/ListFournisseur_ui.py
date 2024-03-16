# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListFournisseur.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FournisseurList(object):
    def setupUi(self, FournisseurList):
        FournisseurList.setObjectName("FournisseurList")
        FournisseurList.setEnabled(True)
        FournisseurList.resize(660, 452)
        self.gridLayout = QtWidgets.QGridLayout(FournisseurList)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(FournisseurList)
        self.label_5.setMinimumSize(QtCore.QSize(190, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(FournisseurList)
        self.label.setMinimumSize(QtCore.QSize(85, 27))
        self.label.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.chercher_lineEdit = QtWidgets.QLineEdit(FournisseurList)
        self.chercher_lineEdit.setMinimumSize(QtCore.QSize(220, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chercher_lineEdit.setFont(font)
        self.chercher_lineEdit.setObjectName("chercher_lineEdit")
        self.horizontalLayout_2.addWidget(self.chercher_lineEdit)
        self.ajouter_pushButton = QtWidgets.QPushButton(FournisseurList)
        self.ajouter_pushButton.setMinimumSize(QtCore.QSize(70, 27))
        self.ajouter_pushButton.setObjectName("ajouter_pushButton")
        self.horizontalLayout_2.addWidget(self.ajouter_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(FournisseurList)
        self.label_3.setMinimumSize(QtCore.QSize(85, 27))
        self.label_3.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.coloneOrdoner_comboBox = QtWidgets.QComboBox(FournisseurList)
        self.coloneOrdoner_comboBox.setMinimumSize(QtCore.QSize(70, 27))
        self.coloneOrdoner_comboBox.setMaximumSize(QtCore.QSize(70, 27))
        self.coloneOrdoner_comboBox.setEditable(False)
        self.coloneOrdoner_comboBox.setObjectName("coloneOrdoner_comboBox")
        self.coloneOrdoner_comboBox.addItem("")
        self.coloneOrdoner_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.coloneOrdoner_comboBox)
        self.directionOrdre_comboBox = QtWidgets.QComboBox(FournisseurList)
        self.directionOrdre_comboBox.setMinimumSize(QtCore.QSize(70, 27))
        self.directionOrdre_comboBox.setMaximumSize(QtCore.QSize(70, 27))
        self.directionOrdre_comboBox.setEditable(False)
        self.directionOrdre_comboBox.setObjectName("directionOrdre_comboBox")
        self.directionOrdre_comboBox.addItem("")
        self.directionOrdre_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.directionOrdre_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fournisseur_tableWidget = QtWidgets.QTableWidget(FournisseurList)
        self.fournisseur_tableWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.fournisseur_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fournisseur_tableWidget.setAlternatingRowColors(True)
        self.fournisseur_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.fournisseur_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fournisseur_tableWidget.setShowGrid(False)
        self.fournisseur_tableWidget.setCornerButtonEnabled(True)
        self.fournisseur_tableWidget.setObjectName("fournisseur_tableWidget")
        self.fournisseur_tableWidget.setColumnCount(4)
        self.fournisseur_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseur_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseur_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseur_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fournisseur_tableWidget.setHorizontalHeaderItem(3, item)
        self.fournisseur_tableWidget.horizontalHeader().setVisible(True)
        self.fournisseur_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.fournisseur_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.fournisseur_tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.fournisseur_tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(FournisseurList)
        self.label_2.setMinimumSize(QtCore.QSize(85, 27))
        self.label_2.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.fournisseurParPage_comboBox = QtWidgets.QComboBox(FournisseurList)
        self.fournisseurParPage_comboBox.setMinimumSize(QtCore.QSize(70, 27))
        self.fournisseurParPage_comboBox.setMaximumSize(QtCore.QSize(70, 27))
        self.fournisseurParPage_comboBox.setEditable(False)
        self.fournisseurParPage_comboBox.setObjectName("fournisseurParPage_comboBox")
        self.fournisseurParPage_comboBox.addItem("")
        self.fournisseurParPage_comboBox.addItem("")
        self.fournisseurParPage_comboBox.addItem("")
        self.fournisseurParPage_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.fournisseurParPage_comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.supprimer_pushButton = QtWidgets.QPushButton(FournisseurList)
        self.supprimer_pushButton.setMinimumSize(QtCore.QSize(70, 27))
        self.supprimer_pushButton.setObjectName("supprimer_pushButton")
        self.horizontalLayout_3.addWidget(self.supprimer_pushButton)
        self.modifier_pushButton = QtWidgets.QPushButton(FournisseurList)
        self.modifier_pushButton.setMinimumSize(QtCore.QSize(70, 27))
        self.modifier_pushButton.setObjectName("modifier_pushButton")
        self.horizontalLayout_3.addWidget(self.modifier_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(FournisseurList)
        QtCore.QMetaObject.connectSlotsByName(FournisseurList)

    def retranslateUi(self, FournisseurList):
        _translate = QtCore.QCoreApplication.translate
        FournisseurList.setWindowTitle(_translate("FournisseurList", "List des fournisseurs"))
        self.label_5.setText(_translate("FournisseurList", "List des fournisseurs"))
        self.label.setText(_translate("FournisseurList", "Chercher"))
        self.ajouter_pushButton.setText(_translate("FournisseurList", "Ajouter"))
        self.label_3.setText(_translate("FournisseurList", "Ordonner par"))
        self.coloneOrdoner_comboBox.setItemText(0, _translate("FournisseurList", "Nom"))
        self.coloneOrdoner_comboBox.setItemText(1, _translate("FournisseurList", "Prenom"))
        self.directionOrdre_comboBox.setItemText(0, _translate("FournisseurList", "Ascendant"))
        self.directionOrdre_comboBox.setItemText(1, _translate("FournisseurList", "Descendant"))
        item = self.fournisseur_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FournisseurList", "ID"))
        item = self.fournisseur_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FournisseurList", "Nom"))
        item = self.fournisseur_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FournisseurList", "Prenom"))
        item = self.fournisseur_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FournisseurList", "Num"))
        self.label_2.setText(_translate("FournisseurList", "Par page"))
        self.fournisseurParPage_comboBox.setItemText(0, _translate("FournisseurList", "10"))
        self.fournisseurParPage_comboBox.setItemText(1, _translate("FournisseurList", "25"))
        self.fournisseurParPage_comboBox.setItemText(2, _translate("FournisseurList", "50"))
        self.fournisseurParPage_comboBox.setItemText(3, _translate("FournisseurList", "All"))
        self.supprimer_pushButton.setText(_translate("FournisseurList", "Supprimer"))
        self.modifier_pushButton.setText(_translate("FournisseurList", "Modifier"))
