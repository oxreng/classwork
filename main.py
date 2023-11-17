import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
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
        qp.save()
        qp.setBrush(QColor(255, 255, 0))
        x_0, y_0, l = randint(0, 700), randint(0, 500), randint(10, 100)
        self.coords.append((x_0, y_0, l))
        for kor in self.coords:
            x_0, y_0, l = kor[0], kor[1], kor[2]
            qp.drawEllipse(x_0, y_0, l, l)
        qp.restore()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
