# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addWidget(object):
    def setupUi(self, addWidget):
        addWidget.setObjectName("addWidget")
        addWidget.resize(444, 212)
        self.gridLayout = QtWidgets.QGridLayout(addWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(addWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(addWidget)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.nomFournisseur_lineEdit = QtWidgets.QLineEdit(addWidget)
        self.nomFournisseur_lineEdit.setObjectName("nomFournisseur_lineEdit")
        self.horizontalLayout_3.addWidget(self.nomFournisseur_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(addWidget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.prenomFournisseur_lineEdit = QtWidgets.QLineEdit(addWidget)
        self.prenomFournisseur_lineEdit.setObjectName("prenomFournisseur_lineEdit")
        self.horizontalLayout_4.addWidget(self.prenomFournisseur_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(addWidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.numFournisseur_lineEdit = QtWidgets.QLineEdit(addWidget)
        self.numFournisseur_lineEdit.setObjectName("numFournisseur_lineEdit")
        self.horizontalLayout_5.addWidget(self.numFournisseur_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(addWidget)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.addressFournisseur_lineEdit = QtWidgets.QLineEdit(addWidget)
        self.addressFournisseur_lineEdit.setObjectName("addressFournisseur_lineEdit")
        self.horizontalLayout_6.addWidget(self.addressFournisseur_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.annulerAjouter_pushButton = QtWidgets.QPushButton(addWidget)
        self.annulerAjouter_pushButton.setObjectName("annulerAjouter_pushButton")
        self.horizontalLayout.addWidget(self.annulerAjouter_pushButton)
        self.ajouterPlus_pushButton = QtWidgets.QPushButton(addWidget)
        self.ajouterPlus_pushButton.setObjectName("ajouterPlus_pushButton")
        self.horizontalLayout.addWidget(self.ajouterPlus_pushButton)
        self.ajouter_pushButton = QtWidgets.QPushButton(addWidget)
        self.ajouter_pushButton.setObjectName("ajouter_pushButton")
        self.horizontalLayout.addWidget(self.ajouter_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)

        self.retranslateUi(addWidget)
        QtCore.QMetaObject.connectSlotsByName(addWidget)

    def retranslateUi(self, addWidget):
        _translate = QtCore.QCoreApplication.translate
        addWidget.setWindowTitle(_translate("addWidget", "Form"))
        self.label.setText(_translate("addWidget", "Ajouter nouveau fournisseur"))
        self.label_3.setText(_translate("addWidget", "Nom"))
        self.label_2.setText(_translate("addWidget", "Prenom"))
        self.label_4.setText(_translate("addWidget", "Num tél"))
        self.label_5.setText(_translate("addWidget", "Address"))
        self.annulerAjouter_pushButton.setText(_translate("addWidget", "Annuler"))
        self.ajouterPlus_pushButton.setText(_translate("addWidget", "Ajouter et continuer"))
        self.ajouter_pushButton.setText(_translate("addWidget", "Ajouter"))
