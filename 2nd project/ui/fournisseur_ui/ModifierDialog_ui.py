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
        Dialog.resize(1035, 464)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"QLineEdit{\n"
"border-radius:3px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #d1d1d1;\n"
"    padding:5px 12px\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("QLineEdit{\n"
"border-radius:3px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #d1d1d1;\n"
"    padding:5px 8px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(85, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(85, 27))
        self.label_3.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.num_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.num_lineEdit.setMinimumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_lineEdit.setFont(font)
        self.num_lineEdit.setStyleSheet("")
        self.num_lineEdit.setObjectName("num_lineEdit")
        self.horizontalLayout_4.addWidget(self.num_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(85, 27))
        self.label_4.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.status_checkBox = QtWidgets.QCheckBox(self.frame)
        self.status_checkBox.setMinimumSize(QtCore.QSize(220, 27))
        self.status_checkBox.setObjectName("status_checkBox")
        self.horizontalLayout_5.addWidget(self.status_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
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
        self.prenom_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.prenom_lineEdit.setMinimumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prenom_lineEdit.setFont(font)
        self.prenom_lineEdit.setObjectName("prenom_lineEdit")
        self.horizontalLayout_3.addWidget(self.prenom_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.status_label = QtWidgets.QLabel(self.frame)
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_6.addWidget(self.status_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.annuler_pushButton = QtWidgets.QPushButton(self.frame)
        self.annuler_pushButton.setMinimumSize(QtCore.QSize(100, 32))
        self.annuler_pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.annuler_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.annuler_pushButton.setStyleSheet("background-color: transparent;\n"
"border:1px solid red;\n"
"border-radius:3px;\n"
"color:red;\n"
"font-weight:500;\n"
"letter-spacing:1px;\n"
"padding:8px 12px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.annuler_pushButton.setIcon(icon)
        self.annuler_pushButton.setObjectName("annuler_pushButton")
        self.horizontalLayout_6.addWidget(self.annuler_pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.modifier_pushButton = QtWidgets.QPushButton(self.frame)
        self.modifier_pushButton.setMinimumSize(QtCore.QSize(110, 32))
        self.modifier_pushButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.modifier_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.modifier_pushButton.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #33b249;\n"
"border-radius:3px;\n"
"color:#33b249;\n"
"font-weight:500;\n"
"letter-spacing:1px;\n"
"padding:8px 12px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/edit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifier_pushButton.setIcon(icon1)
        self.modifier_pushButton.setObjectName("modifier_pushButton")
        self.horizontalLayout_6.addWidget(self.modifier_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(85, 27))
        self.label.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 66, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Modifier un fournisseur"))
        self.label_3.setText(_translate("Dialog", "Num"))
        self.label_4.setText(_translate("Dialog", "Status"))
        self.status_checkBox.setText(_translate("Dialog", "Desactiver"))
        self.label_2.setText(_translate("Dialog", "Prenom"))
        self.annuler_pushButton.setText(_translate("Dialog", "Annuler"))
        self.modifier_pushButton.setText(_translate("Dialog", "Modifier"))
        self.label.setText(_translate("Dialog", "Nom"))
from ui.resources import resources_rc
