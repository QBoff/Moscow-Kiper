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
        uic.loadUi(join("task5", "pop.ui"), self)


class EditInfo(QWidget):
    def __init__(self, id) -> None:
        super().__init__()
        uic.loadUi(join("task5", "pop.ui"), self)
        self.id = id
        self.edit.clicked.connect(self.update)
    
    def update(self):
        db = sqlite3.connect(join("task5", "coffee.sqlite"))
        cur = db.cursor()
        try:
            name = self.bookTitle.text()
            elem1 = self.bookAuthor.text()
            elem2 = self.bookReleaseYear.text()
            desc = self.bookGenre.text()
            for i in [name, elem1, elem2, desc]:
                if not (bool(i) and bool(i.strip())):
                    raise ValueError
                for w in i:
                    if w.isdigit():
                        raise ValueError
            
            cs = float(self.costl.text())
            vl = float(self.volumel.text())
        except ValueError:
            self.errors.setText("Введены некорректные данные!!!")
        else:
            cur.execute(f'''
                        UPDATE coffee SET name_of_the_variety = ?, degree_of_roasting = ?,
                        ground_or_in_grains = ?,
                        taste_description = ?, cost = ?, packing_volume = ?

                        WHERE id = ?''',
                        [name, elem1, elem2, desc, cs, vl, self.id])

            db.commit()
            db.close()
    
    def addNewCoffeeSort(self):
        # req = INSERT INTO coffee (name_of_the_variety, degree_of_roasting, ground_or_in_grains, taste_description, cost, packing_volume)
        # VALUES ("1", "1", "1", "1", 1, 1)
        db = sqlite3.connect(join("task5", "coffee.sqlite"))
        cur = db.cursor()
        try:
            name = self.bookTitle.text()
            elem1 = self.bookAuthor.text()
            elem2 = self.bookReleaseYear.text()
            desc = self.bookGenre.text()
            for i in [name, elem1, elem2, desc]:
                if not (bool(i) and bool(i.strip())):
                    raise ValueError
                for w in i:
                    if w.isdigit():
                        raise ValueError
            
            cs = float(self.costl.text())
            vl = float(self.volumel.text())
        except ValueError:
            self.errors.setText("Введены некорректные данные!!!")
        
        cur.execute(f'''
                    INSERT INTO coffee (name_of_the_variety, degree_of_roasting, ground_or_in_grains, taste_description, cost, packing_volume)
                    VALUES (?, ?, ?, ?, ?, ?)''',
                    [name, elem1, elem2, desc, cs, vl])

        db.commit()
        db.close()

class AddNewInfo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(join("task5", "pop2.ui"), self)
        self.add.clicked.connect(self.addNewItem)
    
    def addNewItem(self):
        db = sqlite3.connect(join("task5", "coffee.sqlite"))
        cur = db.cursor()
        try:
            name = self.bookTitle.text()
            elem1 = self.bookAuthor.text()
            elem2 = self.bookReleaseYear.text()
            desc = self.bookGenre.text()
            for i in [name, elem1, elem2, desc]:
                if not (bool(i) and bool(i.strip())):
                    raise ValueError
                for w in i:
                    if w.isdigit():
                        raise ValueError
            
            cs = float(self.costl.text())
            vl = float(self.volumel.text())
        except ValueError:
            self.errors.setText("Введены некорректные данные!!!")
        else:
            cur.execute(f'''
                        INSERT INTO coffee (name_of_the_variety, degree_of_roasting, ground_or_in_grains, taste_description, cost, packing_volume)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                        [name, elem1, elem2, desc, cs, vl])

            db.commit()
            db.close()
        


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(join("task5", "main.ui"), self)
        self.btn.clicked.connect(self.search)
        self.addNewCoffe.clicked.connect(self.addSomeInfo)
        

    def search(self):
        self.listWidget.clear()
        # searchText = self.lineEdit.text()
        # db = sqlite3.connect(join("QT_Standalone", "task7", "books.db"))
        db = sqlite3.connect(join("task5", "coffee.sqlite"))
        cur = db.cursor()
        res = cur.execute(
            f'''SELECT * FROM coffee''')

        for elem in res:
            # print(elem)
            btn = QPushButton(f"{elem[1]}(нажми для большей информации)", self)

            clickFunc = partial(self.some, elem[0], elem[1],
                                elem[2], elem[3], elem[4], elem[5], elem[6])
            btn.clicked.connect(clickFunc)

            item = QListWidgetItem()
            item.setSizeHint(btn.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, btn)

    def some(self, id, name, author, year, genre, cost, volume):
        self.pop = EditInfo(id)
        # там снизу есть нужные поля для ввода
        self.pop.bookAuthor.setText(author)
        self.pop.bookTitle.setText(name)
        self.pop.bookGenre.setText(genre)
        self.pop.bookReleaseYear.setText(str(year))
        self.pop.costl.setText(str(cost))
        self.pop.volumel.setText(str(volume))

        self.pop.show()
    
    def addSomeInfo(self):
        self.pop2 = AddNewInfo()
        self.pop2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())