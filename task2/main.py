import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
import random


class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.initUi()
    
    def initUi(self):
        
        self.setGeometry(550, 200, 800, 600)
        self.setWindowTitle("Simple Window")
        self.paint = False
        self.btn = QPushButton("Нажми", self)
        self.btn.resize(150, 60)
        self.btn.move(30, 20)
        self.btn.clicked.connect(self.doPaint)
    
    def drawEllipse(self, qp):
        qp.setBrush(QColor(255, 237, 0))
        width, height = QMainWindow.width(self), QMainWindow.height(self)
        if width <= 200 and height <= 150:
            print("This window is too small for me")
            return
        
        for i in range(2):
            radius = random.randrange(30, 150)
            random_cors = random.randrange(0, min(width, height) - radius)
            qp.drawEllipse(random_cors, random_cors, radius, radius)
    
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
