# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(653, 447)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(190, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(85, 27))
        self.label.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.chercher_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.chercher_lineEdit.setMinimumSize(QtCore.QSize(220, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chercher_lineEdit.setFont(font)
        self.chercher_lineEdit.setObjectName("chercher_lineEdit")
        self.horizontalLayout_2.addWidget(self.chercher_lineEdit)
        self.ajouter_pushButton = QtWidgets.QPushButton(self.frame)
        self.ajouter_pushButton.setMinimumSize(QtCore.QSize(70, 27))
        self.ajouter_pushButton.setObjectName("ajouter_pushButton")
        self.horizontalLayout_2.addWidget(self.ajouter_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(85, 27))
        self.label_3.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.coloneOrdoner_comboBox = QtWidgets.QComboBox(self.frame)
        self.coloneOrdoner_comboBox.setMinimumSize(QtCore.QSize(70, 27))
        self.coloneOrdoner_comboBox.setMaximumSize(QtCore.QSize(70, 27))
        self.coloneOrdoner_comboBox.setEditable(False)
        self.coloneOrdoner_comboBox.setObjectName("coloneOrdoner_comboBox")
        self.coloneOrdoner_comboBox.addItem("")
        self.coloneOrdoner_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.coloneOrdoner_comboBox)
        self.directionOrdre_comboBox = QtWidgets.QComboBox(self.frame)
        self.directionOrdre_comboBox.setMinimumSize(QtCore.QSize(70, 27))
        self.directionOrdre_comboBox.setMaximumSize(QtCore.QSize(70, 27))
        self.directionOrdre_comboBox.setEditable(False)
        self.directionOrdre_comboBox.setObjectName("directionOrdre_comboBox")
        self.directionOrdre_comboBox.addItem("")
        self.directionOrdre_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.directionOrdre_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.item_tableWidget = QtWidgets.QTableWidget(self.frame)
        self.item_tableWidget.setMinimumSize(QtCore.QSize(0, 320))
        self.item_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.item_tableWidget.setAlternatingRowColors(True)
        self.item_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.item_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.item_tableWidget.setShowGrid(False)
        self.item_tableWidget.setCornerButtonEnabled(True)
        self.item_tableWidget.setObjectName("item_tableWidget")
        self.item_tableWidget.setColumnCount(6)
        self.item_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.item_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_tableWidget.setHorizontalHeaderItem(5, item)
        self.item_tableWidget.horizontalHeader().setVisible(True)
        self.item_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.item_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.item_tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.item_tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(85, 27))
        self.label_2.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.rowParPage_comboBox = QtWidgets.QComboBox(self.frame)
        self.rowParPage_comboBox.setMinimumSize(QtCore.QSize(70, 27))
        self.rowParPage_comboBox.setMaximumSize(QtCore.QSize(70, 27))
        self.rowParPage_comboBox.setEditable(False)
        self.rowParPage_comboBox.setObjectName("rowParPage_comboBox")
        self.rowParPage_comboBox.addItem("")
        self.rowParPage_comboBox.addItem("")
        self.rowParPage_comboBox.addItem("")
        self.rowParPage_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.rowParPage_comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.supprimer_pushButton = QtWidgets.QPushButton(self.frame)
        self.supprimer_pushButton.setMinimumSize(QtCore.QSize(70, 27))
        self.supprimer_pushButton.setObjectName("supprimer_pushButton")
        self.horizontalLayout_3.addWidget(self.supprimer_pushButton)
        self.modifier_pushButton = QtWidgets.QPushButton(self.frame)
        self.modifier_pushButton.setMinimumSize(QtCore.QSize(70, 27))
        self.modifier_pushButton.setObjectName("modifier_pushButton")
        self.horizontalLayout_3.addWidget(self.modifier_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "List des items"))
        self.label.setText(_translate("Form", "Chercher"))
        self.ajouter_pushButton.setText(_translate("Form", "Ajouter"))
        self.label_3.setText(_translate("Form", "Ordonner par"))
        self.coloneOrdoner_comboBox.setItemText(0, _translate("Form", "Nom"))
        self.coloneOrdoner_comboBox.setItemText(1, _translate("Form", "Prenom"))
        self.directionOrdre_comboBox.setItemText(0, _translate("Form", "Ascendant"))
        self.directionOrdre_comboBox.setItemText(1, _translate("Form", "Descendant"))
        item = self.item_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.item_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nom"))
        item = self.item_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Quantité"))
        item = self.item_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Cout"))
        item = self.item_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Date ajout"))
        item = self.item_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Désignation"))
        self.label_2.setText(_translate("Form", "Par page"))
        self.rowParPage_comboBox.setItemText(0, _translate("Form", "10"))
        self.rowParPage_comboBox.setItemText(1, _translate("Form", "25"))
        self.rowParPage_comboBox.setItemText(2, _translate("Form", "50"))
        self.rowParPage_comboBox.setItemText(3, _translate("Form", "All"))
        self.supprimer_pushButton.setText(_translate("Form", "Supprimer"))
        self.modifier_pushButton.setText(_translate("Form", "Modifier"))
