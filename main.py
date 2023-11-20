import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.coffee_table = QtWidgets.QTableWidget(self.centralwidget)
        self.coffee_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.coffee_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.coffee_table.setTabKeyNavigation(True)
        self.coffee_table.setProperty("showDropIndicator", True)
        self.coffee_table.setDragEnabled(False)
        self.coffee_table.setDragDropOverwriteMode(True)
        self.coffee_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.coffee_table.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.coffee_table.setAlternatingRowColors(False)
        self.coffee_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.coffee_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.coffee_table.setObjectName("coffee_table")
        self.coffee_table.setColumnCount(0)
        self.coffee_table.setRowCount(0)
        self.coffee_table.horizontalHeader().setVisible(True)
        self.coffee_table.horizontalHeader().setCascadingSectionResizes(False)
        self.coffee_table.horizontalHeader().setHighlightSections(True)
        self.coffee_table.horizontalHeader().setSortIndicatorShown(False)
        self.coffee_table.horizontalHeader().setStretchLastSection(False)
        self.coffee_table.verticalHeader().setCascadingSectionResizes(False)
        self.coffee_table.verticalHeader().setHighlightSections(True)
        self.coffee_table.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.coffee_table, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эспрессо"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.update_coffee()

    def update_coffee(self):
        self.coffee_table.clearContents()
        result = self.cur.execute("""SELECT coffee.id, types.title, coffee.degree, coffee.in_what, 
        coffee.description, coffee.price, coffee.amount FROM coffee 
        LEFT JOIN types ON types.id = coffee.type""").fetchall()
        self.coffee_table.setRowCount(len(result))
        self.coffee_table.setColumnCount(len(result[0]))
        self.coffee_table.setHorizontalHeaderLabels(
            ['ID', "Название сорта", "Степень обжарки", "Молотый/в зёрнах", "Описание вкуса", "Цена в рублях",
             "Объём упаковки в граммах"])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(val)))
        self.statusbar.showMessage('')
        self.coffee_table.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
