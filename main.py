import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_push = QtWidgets.QPushButton(self.centralwidget)
        self.btn_push.setGeometry(QtCore.QRect(320, 500, 141, 41))
        self.btn_push.setObjectName("btn_push")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и желтые окружности"))
        self.btn_push.setText(_translate("MainWindow", "Сделать кружок"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coords = []
        self.do_paint = False
        self.btn_push.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_krug(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_krug(self, qp):
        x_0, y_0, l = randint(0, 700), randint(0, 500), randint(10, 100)
        self.coords.append((x_0, y_0, l, (randint(0, 255), randint(0, 255), randint(0, 255))))
        for kor in self.coords:
            qp.setBrush(QColor(*kor[3]))
            x_0, y_0, l = kor[0], kor[1], kor[2]
            qp.drawEllipse(x_0, y_0, l, l)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
