from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton , QFrame , QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt ,QPropertyAnimation,QRect
import sys
import subprocess
from PyQt5.QtCore import QTimer


app = QtWidgets.QApplication(sys.argv)

window = QWidget(flags=Qt.FramelessWindowHint)
window.setGeometry(65 , 440 , 687 , 278)
window.setStyleSheet('background-color:#fff')


p1 = QtWidgets.QLabel(window)
p2 = QtWidgets.QLabel(window)
p3 = QtWidgets.QLabel(window)

def part1():      
    pixmap = QPixmap('./icon/Group 12.svg').scaled(182,66)
    p1.setPixmap(pixmap)
    p1.resize(pixmap.width(),pixmap.height())
    p1.move(261,57)

def part2():      
    pixmap = QPixmap('./icon/Group 13.svg').scaled(198,165)
    p2.setPixmap(pixmap)
    p2.resize(pixmap.width(),pixmap.height())
    p2.move(245,57)

def part3():      
    pixmap = QPixmap('./icon/Group 11.svg').scaled(198,165)
    p3.setPixmap(pixmap)
    p3.resize(pixmap.width(),pixmap.height())
    p3.move(245,57)
    p1.hide()
    p2.hide()


def switch():
    window.close()
    run_voice()


timer1 = QTimer()
timer1.timeout.connect(part1)
timer1.start(300)

timer2 = QTimer()
timer2.timeout.connect(part2)
timer2.start(900)

timer3 = QTimer()
timer3.timeout.connect(part3)
timer3.start(1200)

timer4 = QTimer()
timer4.timeout.connect(switch)
timer4.start(2500)

def run_voice():    
        subprocess.call(["python", "../ECHO/home.py"])

window.show()
app.exec_()