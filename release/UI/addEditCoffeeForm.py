# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addEditCoffeeForm(object):
    def setupUi(self, addEditCoffeeForm):
        addEditCoffeeForm.setObjectName("addEditCoffeeForm")
        addEditCoffeeForm.resize(305, 533)
        addEditCoffeeForm.setMinimumSize(QtCore.QSize(0, 0))
        addEditCoffeeForm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(addEditCoffeeForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.type = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type.sizePolicy().hasHeightForWidth())
        self.type.setSizePolicy(sizePolicy)
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 0, 1, 1, 1)
        self.degree = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.degree.sizePolicy().hasHeightForWidth())
        self.degree.setSizePolicy(sizePolicy)
        self.degree.setObjectName("degree")
        self.gridLayout.addWidget(self.degree, 1, 1, 1, 1)
        self.in_what = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_what.sizePolicy().hasHeightForWidth())
        self.in_what.setSizePolicy(sizePolicy)
        self.in_what.setObjectName("in_what")
        self.gridLayout.addWidget(self.in_what, 2, 1, 1, 1)
        self.description = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 3, 1, 1, 1)
        self.price = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price.sizePolicy().hasHeightForWidth())
        self.price.setSizePolicy(sizePolicy)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 4, 1, 1, 1)
        self.amount = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amount.sizePolicy().hasHeightForWidth())
        self.amount.setSizePolicy(sizePolicy)
        self.amount.setObjectName("amount")
        self.gridLayout.addWidget(self.amount, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btn_add_or_edit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_or_edit.sizePolicy().hasHeightForWidth())
        self.btn_add_or_edit.setSizePolicy(sizePolicy)
        self.btn_add_or_edit.setObjectName("btn_add_or_edit")
        self.verticalLayout.addWidget(self.btn_add_or_edit)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        addEditCoffeeForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addEditCoffeeForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 21))
        self.menubar.setObjectName("menubar")
        addEditCoffeeForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addEditCoffeeForm)
        self.statusbar.setObjectName("statusbar")
        addEditCoffeeForm.setStatusBar(self.statusbar)

        self.retranslateUi(addEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(addEditCoffeeForm)

    def retranslateUi(self, addEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        addEditCoffeeForm.setWindowTitle(_translate("addEditCoffeeForm", "Добавить кофе"))
        self.label.setText(_translate("addEditCoffeeForm", "Название сорта"))
        self.label_2.setText(_translate("addEditCoffeeForm", "Степень обжарки"))
        self.label_3.setText(_translate("addEditCoffeeForm", "Молотый/в зёрнах"))
        self.label_4.setText(_translate("addEditCoffeeForm", "Описание вкуса"))
        self.label_5.setText(_translate("addEditCoffeeForm", "Цена"))
        self.label_6.setText(_translate("addEditCoffeeForm", "Объём упаковки"))
        self.btn_add_or_edit.setText(_translate("addEditCoffeeForm", "Добавить"))