import sys
from random import randint as rn
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import QtCore, QtWidgets


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow().setupUi(self)
        self.setFixedSize(800, 600)
        self.paint = False
        self.centralWidget().children()[0].clicked.connect(self.paint_circle)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            c1 = rn(50, 250)
            c2 = rn(50, 250)
            qp.setBrush(QColor(rn(0, 255), rn(0, 255), rn(0, 255)))
            qp.drawEllipse(0, 55, c1, c1)
            qp.setBrush(QColor(rn(0, 255), rn(0, 255), rn(0, 255)))
            qp.drawEllipse(250, 55, c2, c2)
            self.paint = False

    def paint_circle(self):
        self.paint = True
        self.repaint()


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 141, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Круг"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
