# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifierDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 305)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(85, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(85, 27))
        self.label.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(220, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(85, 27))
        self.label_2.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.prenom_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.prenom_lineEdit.setMinimumSize(QtCore.QSize(220, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prenom_lineEdit.setFont(font)
        self.prenom_lineEdit.setObjectName("prenom_lineEdit")
        self.horizontalLayout_2.addWidget(self.prenom_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(85, 27))
        self.label_3.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.num_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.num_lineEdit.setMinimumSize(QtCore.QSize(220, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_lineEdit.setFont(font)
        self.num_lineEdit.setObjectName("num_lineEdit")
        self.horizontalLayout_3.addWidget(self.num_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(85, 27))
        self.label_4.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.status_checkBox = QtWidgets.QCheckBox(Dialog)
        self.status_checkBox.setMinimumSize(QtCore.QSize(220, 27))
        self.status_checkBox.setObjectName("status_checkBox")
        self.horizontalLayout_4.addWidget(self.status_checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.annuler_pushButton = QtWidgets.QPushButton(Dialog)
        self.annuler_pushButton.setMinimumSize(QtCore.QSize(70, 27))
        self.annuler_pushButton.setObjectName("annuler_pushButton")
        self.horizontalLayout_5.addWidget(self.annuler_pushButton)
        self.modifier_pushButton = QtWidgets.QPushButton(Dialog)
        self.modifier_pushButton.setMinimumSize(QtCore.QSize(70, 27))
        self.modifier_pushButton.setObjectName("modifier_pushButton")
        self.horizontalLayout_5.addWidget(self.modifier_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Modifier un fournisseur"))
        self.label.setText(_translate("Dialog", "Nom"))
        self.label_2.setText(_translate("Dialog", "Prenom"))
        self.label_3.setText(_translate("Dialog", "Num"))
        self.label_4.setText(_translate("Dialog", "Status"))
        self.status_checkBox.setText(_translate("Dialog", "Desactiver"))
        self.annuler_pushButton.setText(_translate("Dialog", "Annuler"))
        self.modifier_pushButton.setText(_translate("Dialog", "Modifier"))