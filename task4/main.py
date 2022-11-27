import sys
from os.path import join

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidgetItem, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sqlite3
from functools import partial


class Pop(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(join("task4", "pop.ui"), self)


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(join("task4", "main.ui"), self)
        self.btn.clicked.connect(self.search)
        

    def search(self):
        self.listWidget.clear()
        # searchText = self.lineEdit.text()
        # db = sqlite3.connect(join("QT_Standalone", "task7", "books.db"))
        db = sqlite3.connect(join("task4", "coffee.sqlite"))
        cur = db.cursor()
        res = cur.execute(
            f'''SELECT * FROM coffee''')

        for elem in res:
            # print(elem)
            btn = QPushButton(f"{elem[1]}(нажми для большей информации)", self)

            clickFunc = partial(self.some, elem[1],
                                elem[2], elem[3], elem[4], elem[5], elem[6])
            btn.clicked.connect(clickFunc)

            item = QListWidgetItem()
            item.setSizeHint(btn.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, btn)

    def some(self, name, author, year, genre, cost, volume):
        self.pop = Pop()
        # там снизу есть нужные поля для ввода
        self.pop.bookAuthor.setText(author)
        self.pop.bookTitle.setText(name)
        self.pop.bookGenre.setText(genre)
        self.pop.bookReleaseYear.setText(str(year))
        self.pop.costl.setText(str(cost))
        self.pop.volumel.setText(str(volume))

        self.pop.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())