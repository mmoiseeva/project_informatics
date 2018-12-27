import sys
from random import  randint
from PyQt5.QtWidgets import * #QWidget, QApplication, QLabel
from PyQt5.QtGui import * #QPainter, QColor
from PyQt5 import *
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self. country_list=[['Russia',255,255,255,0,0,255,255,0,0],['Germany',0,0,0,255,0,0,255,255,0],['Estonia',0,0,255,0,0,0,255,255,255],['Armenia',255,0,0,0,0,255,255,69,0],['Bulgaria',255,255,255,46,139,87,255,0,0],['Hungary',255,0,0,255,255,255,46,139,87],['Yemen',255,0,0,255,255,255,0,0,0],['Columbia',255,215,0,0,0,255,255,0,0],['Latvia',255,0,0,255,255,255,255,0,0],['Lithuania',255,215,0,46,139,87,255,0,0],['Luxembourg',255,0,0,255,255,255,32,178,170],['Netherlands',255,0,0,255,255,255,0,0,255]]
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.rez = QLabel(self)
        self.rez.setGeometry(30,0,120,30)
        self.rez.setText("Last Result: None")
        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(10,20,120,23)
        self.button_1.move (30,120)
        self.button_1.clicked.connect(self.run1)
        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(10,20,120,23)
        self.button_2.move (30,140)
        self.button_2.clicked.connect(self.run2)
        self.button_3 = QPushButton(self)
        self.button_3.setGeometry(10,20,120,23)
        self.button_3.move (30,160)
        self.button_3.clicked.connect(self.run3)
        self.c1 = randint(0,len(self.country_list)-1)
        self.chosencountry = self.country_list[self.c1][0]
        self.wrongcountry1 = self.country_list[self.c1-1][0]
        self.wrongcountry2 = self.country_list[self.c1-2][0]
        self.typecontr = randint(0,5)
        self.color1 = QColor(self.country_list[self.c1][1], self.country_list[self.c1][2], self.country_list[self.c1][3])
        self.color2 = QColor(self.country_list[self.c1][4], self.country_list[self.c1][5], self.country_list[self.c1][6])
        self.color3 = QColor(self.country_list[self.c1][7], self.country_list[self.c1][8], self.country_list[self.c1][9])
        self.show()
 
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()
 
    def drawFlag(self,qp):
        qp.setBrush(self.color1)
        qp.drawRect(30, 30 + 0, 120, 30)
        qp.setBrush(self.color2)
        qp.drawRect(30, 30 + 30, 120, 30)
        qp.setBrush(self.color3)
        qp.drawRect(30, 30 + 60, 120, 30)
        if self.typecontr == 0:
            self.button_1.setText(self.chosencountry)
            self.button_2.setText(self.wrongcountry1)
            self.button_3.setText(self.wrongcountry2)
        elif self.typecontr == 1:
            self.button_1.setText(self.chosencountry)
            self.button_2.setText(self.wrongcountry2)
            self.button_3.setText(self.wrongcountry1)
        elif self.typecontr == 2:
            self.button_1.setText(self.wrongcountry1)
            self.button_2.setText(self.chosencountry)
            self.button_3.setText(self.wrongcountry2)
        elif self.typecontr == 3:
            self.button_1.setText(self.wrongcountry2)
            self.button_2.setText(self.chosencountry)
            self.button_3.setText(self.wrongcountry1)
        elif self.typecontr == 4:
            self.button_1.setText(self.wrongcountry1)
            self.button_2.setText(self.wrongcountry2)
            self.button_3.setText(self.chosencountry)
        elif self.typecontr == 5:
            self.button_1.setText(self.wrongcountry2)
            self.button_2.setText(self.wrongcountry1)
            self.button_3.setText(self.chosencountry)
 
    def run1(self):
        if self.typecontr == 0 or self.typecontr == 1:
            self.rez.setText("Last Result: True")
        else:
            self.rez.setText("Last Result: False")
        self.c1 = randint(0,len(self.country_list)-1)
        self.chosencountry = self.country_list[self.c1][0]
        self.wrongcountry1 = self.country_list[self.c1-1][0]
        self.wrongcountry2 = self.country_list[self.c1-2][0]
        self.typecontr = randint(0,5)
        self.color1 = QColor(self.country_list[self.c1][1], self.country_list[self.c1][2], self.country_list[self.c1][3])
        self.color2 = QColor(self.country_list[self.c1][4], self.country_list[self.c1][5], self.country_list[self.c1][6])
        self.color3 = QColor(self.country_list[self.c1][7], self.country_list[self.c1][8], self.country_list[self.c1][9])
 
    def run2(self):
        if self.typecontr == 2 or self.typecontr == 3:
            self.rez.setText("Last Result: True")
        else:
            self.rez.setText("Last Result: False")
        self.c1 = randint(0,len(self.country_list)-1)
        self.chosencountry = self.country_list[self.c1][0]
        self.wrongcountry1 = self.country_list[self.c1-1][0]
        self.wrongcountry2 = self.country_list[self.c1-2][0]
        self.typecontr = randint(0,5)
        self.color1 = QColor(self.country_list[self.c1][1], self.country_list[self.c1][2], self.country_list[self.c1][3])
        self.color2 = QColor(self.country_list[self.c1][4], self.country_list[self.c1][5], self.country_list[self.c1][6])
        self.color3 = QColor(self.country_list[self.c1][7], self.country_list[self.c1][8], self.country_list[self.c1][9])
 
    def run3(self):
        if self.typecontr == 4 or self.typecontr == 5:
            self.rez.setText("Last Result: True")
        else:
            self.rez.setText("Last Result: False")
        self.c1 = randint(0,len(self.country_list)-1)
        self.chosencountry = self.country_list[self.c1][0]
        self.wrongcountry1 = self.country_list[self.c1-1][0]
        self.wrongcountry2 = self.country_list[self.c1-2][0]
        self.typecontr = randint(0,5)
        self.color1 = QColor(self.country_list[self.c1][1], self.country_list[self.c1][2], self.country_list[self.c1][3])
        self.color2 = QColor(self.country_list[self.c1][4], self.country_list[self.c1][5], self.country_list[self.c1][6])
        self.color3 = QColor(self.country_list[self.c1][7], self.country_list[self.c1][8], self.country_list[self.c1][9])
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
