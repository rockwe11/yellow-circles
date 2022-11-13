import sys
from random import randint as rn
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        uic.loadUi("UI.ui", self)
        self.paint = False
        self.pushButton.clicked.connect(self.paint_circle)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            c1 = rn(50, 250)
            c2 = rn(50, 250)
            qp.drawEllipse(0, 55, c1, c1)
            qp.drawEllipse(250, 55, c2, c2)
            self.paint = False

    def paint_circle(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())