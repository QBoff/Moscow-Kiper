import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from os.path import join

import random


class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(join("task2", "main.ui"), self)

        self.btn.clicked.connect(self.doPaint)
        self.paint = False

    def drawEllipse(self, qp):
        qp.setBrush(self.getColor())
        width, height = QMainWindow.width(self), QMainWindow.height(self)

        othercorsx, othercorsy = set(), set()

        radius = random.randrange(50, 200)
        cors = random.randrange(
            0, width - 2 * radius), random.randrange(0, height - 2 * radius)
        othercorsx = set(range(cors[0], cors[0] + radius + 1))
        othercorsy = set(range(cors[1], cors[1] + radius + 1))
        qp.drawEllipse(cors[0], cors[1], radius, radius)

        radius = random.randrange(50, 200)
        cors = random.randrange(
            0, width - 2 * radius), random.randrange(0, height - 2 * radius)

        while set(range(cors[0], cors[0] + radius + 1)) & othercorsx != set() and \
                set(range(cors[1], cors[1] + radius + 1)) & othercorsy != set():
            cors = random.randrange(
                0, width - 2 * radius), random.randrange(0, height - 2 * radius)

        qp.drawEllipse(cors[0], cors[1], radius, radius)

    def getColor(self):
        return QColor(255, 255, 0)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.drawEllipse(qp)
            qp.end()
            self.paint = False

    def doPaint(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())
