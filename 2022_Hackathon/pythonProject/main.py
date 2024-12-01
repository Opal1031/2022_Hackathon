import sys
import logging
import os

import pandas as pd
import pymysql
import pandas
import dbConnect

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt



class MyWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(200, 200, 1500, 800)
<<<<<<< HEAD
=======
        self.setWindowTitle("야 너도 선곡 할 수 있어")
>>>>>>> 113d11406f9becd904cc6f55b6641afc933c5a1f

    def initUI(self):
        octLists = ['2옥파', '2옥파#', '2옥솔',
                    '2옥솔#', '2옥라', '2옥라#',
                    '2옥시', '3옥도', '3옥도#',
                    '3옥레', '3옥레#', '3옥미',
                    '3옥파', '3옥파#', '3옥솔',
                    '3옥솔#']
        categoryLists = ['록/메탈', '발라드', '인디음악',
                         '포크/블루스', '댄스', '국내드라마',
                         'R&B/Soul', '뉴에이지', 'POP',
                         '랩/힙합', '애니메이션/웹툰', ]


        #성별 버튼
        self.radio1 = QRadioButton("남성", self)
        self.resize(100, 50)
        self.radio1.move(100, 100)
        self.radio1.setChecked(False)
        self.radio1.toggled.connect(self.radio_fun)

        self.radio2 = QRadioButton("여성", self)
        self.radio2.resize(100, 50)
        self.radio2.move(200, 87)
        self.radio1.setChecked(False)
        self.radio2.toggled.connect(self.radio_fun)

        #옥타브 버튼 move(x,y)
        bOct = QComboBox(self)
        for i in octLists:
            bOct.addItem(i)
        bOct.resize(200, 50)
        bOct.move(100, 150)
        bOct.currentTextChanged.connect(self.octBox_changed)

        #장르 버튼
        bCategory = QComboBox(self)
        for i in categoryLists:
            bCategory.addItem(i)
        bCategory.resize(200, 50)
        bCategory.move(100, 225)
        bCategory.currentTextChanged.connect(self.cateBox_changed)

        #입력 버튼
        btn = QPushButton("입력", self)
        btn.resize(200, 50)
        btn.move(100, 325)
        btn.clicked.connect(self.surprise)


        self.label1 = QLabel("곡 정보", self)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.resize(400, 50)
        self.label1.move(700, 200)

    def radio_fun(self, checked):
        global gend
        gend =""
        if checked:
            if self.radio1.isChecked():
                gend="M"
            elif self.radio2.isChecked():
                gend="F"

    def octBox_changed(self, item):
        global octName
        octName = item

    def cateBox_changed(self, item):
        global cateName
        cateName = item

    def surprise(self):
        print(gend)
        print(octName)
        print(cateName)
        dif = dbConnect.pyQTConnect(gend, octName, cateName)

        print(dif)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

# 해당 코드 실행 시 부터 이벤트 루프 발생
app.exec_()

print("루프 밖")