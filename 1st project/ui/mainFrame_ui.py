# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        self.menuEmployee = QtWidgets.QMenu(self.menubar)
        self.menuEmployee.setObjectName("menuEmployee")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuStock = QtWidgets.QMenu(self.menubar)
        self.menuStock.setObjectName("menuStock")
        MainWindow.setMenuBar(self.menubar)
        self.actionList = QtWidgets.QAction(MainWindow)
        self.actionList.setObjectName("actionList")
        self.actionAjouter = QtWidgets.QAction(MainWindow)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionList_2 = QtWidgets.QAction(MainWindow)
        self.actionList_2.setObjectName("actionList_2")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.itemList_action = QtWidgets.QAction(MainWindow)
        self.itemList_action.setObjectName("itemList_action")
        self.ajouterTransactions_action = QtWidgets.QAction(MainWindow)
        self.ajouterTransactions_action.setObjectName("ajouterTransactions_action")
        self.menuEmployee.addAction(self.actionList)
        self.menuEmployee.addAction(self.actionAjouter)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuStock.addAction(self.itemList_action)
        self.menuStock.addAction(self.ajouterTransactions_action)
        self.menubar.addAction(self.menuEmployee.menuAction())
        self.menubar.addAction(self.menuStock.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuEmployee.setTitle(_translate("MainWindow", "Employee"))
        self.menuHelp.setTitle(_translate("MainWindow", "Information"))
        self.menuStock.setTitle(_translate("MainWindow", "Stock"))
        self.actionList.setText(_translate("MainWindow", "List"))
        self.actionAjouter.setText(_translate("MainWindow", "Ajouter"))
        self.actionList_2.setText(_translate("MainWindow", "List"))
        self.actionAdd.setText(_translate("MainWindow", "Ajouter"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About DEV"))
        self.itemList_action.setText(_translate("MainWindow", "List"))
        self.ajouterTransactions_action.setText(_translate("MainWindow", "Transactions"))
