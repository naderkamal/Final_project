from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton , QFrame , QVBoxLayout , QListWidget, QListWidgetItem , QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt ,QPropertyAnimation,QRect,QThread,pyqtSignal
import sys

app = QtWidgets.QApplication(sys.argv)
window = QWidget(flags=Qt.WindowCloseButtonHint)  
window.setGeometry(65 , 100 , 1000 , 600)
window.setStyleSheet('background-color:#fff')
window.setWindowTitle("ECHO - Help")
window.setWindowIcon(QIcon("./icon/logo.png"))

# setting 
settingFrame = QFrame(window)
settingFrame.setGeometry( 0 , 0 , 170 , 600)

vbox = QVBoxLayout()
settingFrame.setLayout(vbox)

sVoice = QPushButton('Voice Assistant',window)
sVoiceIcon = QIcon("./icon/mic.png")
sVoice.setIcon(sVoiceIcon)
sVoice.setProperty("class","active")
vbox.addWidget(sVoice)
sVoice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

sMouse = QPushButton('Virutal Mouse',window)
sMouseIcon = QIcon("./icon/mouse.png")
sMouse.setIcon(sMouseIcon)

vbox.addWidget(sMouse)
sMouse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

Skeyboard = QPushButton('Virtual Keyboard',window)
SkeyboardIcon = QIcon("./icon/keyboard.png")
Skeyboard.setIcon(SkeyboardIcon)

vbox.addWidget(Skeyboard)
Skeyboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
sMedia = QPushButton('Media Control',window)
sMediaIcon = QIcon("./icon/control.png")
sMedia.setIcon(sMediaIcon)

vbox.addWidget(sMedia)
sMedia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


settingFrame.setStyleSheet("""
    QFrame{
        background-color:"#048CFC";
        color:"white";
        font-size:14px;
    }
    QPushButton{
        border: none;
        font-size: 16px;
        padding:6px;
        background-color:"#048CFC";
        color: "white"
    }
    .active{
        border-bottom : 1px solid #fff;
    }
""")

# Set title 
title = QtWidgets.QLabel('Voice assistant:',window)
title.move(190,20)
title.setFixedSize(1000, 40)
title.setStyleSheet('font-family: Arial; font-weight: 400; font-size: 32px;')

# Create a QLabel widget to display the unordered list
list_label = QLabel(window)
list_label.setTextFormat(Qt.RichText)
list_label.move(200,60)

list_label.setStyleSheet("""
QLabel{
font-size: 20px;
}
""")

# Set the text with HTML formatting
list_text = "<ol>"
list_text += "<li>Press the microphone button <br></li> "
list_text += "<li>Say 'hello' whenever you need to communicate with the voice assistant <br> </li>"
list_text += "<li>State your command</li>"
list_text += "</ol>"
list_label.setText(list_text)
list_label.setFixedSize(1000,200)

# Create a layout to hold the QLabel
layout = QVBoxLayout()
layout.addWidget(list_label)

def voice(self):
    sMouse.setProperty("class","a")
    Skeyboard.setProperty("class","a")
    sMedia.setProperty("class","a")

    sVoice.setProperty("class","active")

    settingFrame.setStyleSheet("""
    QFrame{
        background-color:"#048CFC";
        color:"white";
        font-size:14px;
    }
    QPushButton{
        border: none;
        font-size: 16px;
        padding:6px;
        background-color:"#048CFC";
        color: "white"
    }
    .active{
    border-bottom: 1px solid #fff
    }
    .a{
    border-bottom: 0px;
    }
    """)

    title.setText('Voice assistant:')
    

    list_text = "<ol>"
    list_text += "<li>Press the microphone button <br></li> "
    list_text += "<li>Say 'hello' whenever you need to communicate with the voice assistant <br> </li>"
    list_text += "<li>State your command</li>"
    list_text += "</ol>"
    list_label.setText(list_text)
    list_label.setFixedSize(1000,200)

sVoice.clicked.connect(voice)


def mouse(self):
    sVoice.setProperty("class","a")
    Skeyboard.setProperty("class","a")
    sMedia.setProperty("class","a")

    sMouse.setProperty("class","active")

    settingFrame.setStyleSheet("""
    QFrame{
        background-color:"#048CFC";
        color:"white";
        font-size:14px;
    }
    QPushButton{
        border: none;
        font-size: 16px;
        padding:6px;
        background-color:"#048CFC";
        color: "white"
    }
    .active{
    border-bottom: 1px solid #fff
    }
    .a{
    border-bottom: 0px;
    }
    """)

    title.setText('Virtual Mouse:')

    list_text = "<ol>"
    list_text += "<li>Press the gear icon <br></li>"
    list_text += "<li>Select the 'virtual mouse' option <br></li>"
    list_text += "<li>Once the virtual mouse screen opens, you can perform various actions <br> using the following instructions: <br> </li>"
    list_text += "<li>Use your middle finger and index finger to move the pointer. <br> </li>"
    list_text += "<li> Bend your middle finger to perform a right click. <br> </li>"
    list_text += "<li>Bend your index finger to perform a left click. <br></li>"
    list_text += "<li>Bend and hold your index finger to perform a double click.<br> - Stretch your middle finger, index finger, and ring finger to scroll up <br>.</li>"
    list_text += "<li>Bend your middle finger, index finger, and ring finger to scroll down.</li>"
    list_text += "</ol>"

    list_label.setText(list_text)
    list_label.setFixedSize(1000,500)

sMouse.clicked.connect(mouse)


def keyboard(self):

    sVoice.setProperty("class","a")
    sMouse.setProperty("class","a")
    sMedia.setProperty("class","a")

    Skeyboard.setProperty("class","active")

    settingFrame.setStyleSheet("""
    QFrame{
        background-color:"#048CFC";
        color:"white";
        font-size:14px;
    }
    QPushButton{
        border: none;
        font-size: 16px;
        padding:6px;
        background-color:"#048CFC";
        color: "white"
    }
    .active{
    border-bottom: 1px solid #fff
    }
    .a{
    border-bottom: 0px;
    }
    """)

    title.setText('Virtual Keyboard :')

    list_text = "<ol>"
    list_text += "<li>Press the gear icon <br></li>"
    list_text += "<li>Select the ' virtual Keyboard ' option <br></li>"
    list_text += "<li>Once the virtual keyboard screen opens, you can: <br> </li>"
    list_text += "<li>Use your middle finger and index finger to move the pointer. <br> </li>"
    list_text += "<li>Bend your index finger to type a letter or perform an action. </li>"
    list_text += "</ol>"

    list_label.setText(list_text)
    list_label.setFixedSize(1000,300)

Skeyboard.clicked.connect(keyboard)


def media(self):
    sVoice.setProperty("class","a")
    sMouse.setProperty("class","a")
    Skeyboard.setProperty("class","a")

    sMedia.setProperty("class","active")

    settingFrame.setStyleSheet("""
    QFrame{
        background-color:"#048CFC";
        color:"white";
        font-size:14px;
    }
    QPushButton{
        border: none;
        font-size: 16px;
        padding:6px;
        background-color:"#048CFC";
        color: "white"
    }
    .active{
    border-bottom: 1px solid #fff
    }
    .a{
    border-bottom: 0px;
    }
    """)

    title.setText('Media Control :')

    list_text = "<ol>"
    list_text += "<li>Press the gear icon <br></li>"
    list_text += "<li>Select the ' media control ' option <br></li>"
    list_text += "<li>Once the media control screen opens, you can perform various actions <br> using the following instructions:<br> </li>"
    list_text += "<li>Stretch your hand to pause or play your media. <br> </li>"
    list_text += "<li>Use your thumb finger to skip forward 5 seconds of your media. <br></li>"
    list_text += "<li>Use your index finger and middle finger to skip back 5 seconds of your media.<br></li>"
    list_text += "<li>Stretch your middle finger, index finger, and ring finger to increase the volume.<br></li>"
    list_text += "<li>Stretch your middle finger, index finger, ring finger,<br> and little finger to decrease the volume.</li>"
    list_text += "</ol>"

    list_label.setText(list_text) 
    list_label.setFixedSize(1000,500)

sMedia.clicked.connect(media)

window.show()
app.exec_()