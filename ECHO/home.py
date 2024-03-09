from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton , QFrame , QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt ,QPropertyAnimation,QRect,QThread,pyqtSignal
import sys
import json
sys.path.insert(0,"../ECHO/code/")

def readData():
      with open("../Echo/code/voice/data.json","r") as json_file:
        data = json.load(json_file)
        title.setText(data)
        print(data)
app = QtWidgets.QApplication(sys.argv)

window = QWidget(flags=Qt.FramelessWindowHint)
window.setGeometry(65 , 440 , 687 , 278)
window.setStyleSheet('background-color:#fff')
logo = QtWidgets.QLabel(window)
pixmap = QPixmap('./icon/logo.png').scaled(30,30)
logo.setPixmap(pixmap)
logo.resize(pixmap.width(),pixmap.height())
logo.move(50,30)

# Set title 
title = QtWidgets.QLabel('Press mic to start',window)
title.setGeometry(180, 100, 400, 100)
# style the title
title.setStyleSheet('font-family: Arial; font-weight: 400; font-size: 22px;')

voice = QPushButton(window)
icon = QIcon("./icon/mic.png")
voice.setIcon(icon)
voice.setFixedSize(41,49)
voice.setIconSize(voice.size())
voice.move(324,198)
voice.setStyleSheet('border-radius: 20px; background-color: #048CFC')
voice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

gear = QPushButton(window)
gearIcon = QIcon("./icon/gear.png")
gear.setIcon(gearIcon)
gear.setFixedSize(29,31)
gear.setIconSize(gear.size())
gear.move(620,30)
gear.setStyleSheet('border: none')
gear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

gearAnimate_1 = QPropertyAnimation(gear , b"geometry")
gearAnimate_1.setDuration(300)
gearAnimate_1.setStartValue(QRect(620,30,29,31))
gearAnimate_1.setEndValue(QRect(445,30,29,31))

gearAnimate_2 = QPropertyAnimation(gear, b"geometry")
gearAnimate_2.setDuration(300)
gearAnimate_2.setStartValue(QRect(445,30,29,31))
gearAnimate_2.setEndValue(QRect(620,30,29,31))
# setting 
settingFrame = QFrame(window)
settingFrame.setGeometry( 690 , 0 , 178 , 278)

vbox = QVBoxLayout()
settingFrame.setLayout(vbox)

sVoice = QPushButton('Voice Assistant',window)
sVoiceIcon = QIcon("./icon/mic.png")
sVoice.setIcon(sVoiceIcon)
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

sHelp = QPushButton('Help',window)
sHelpIcon = QIcon("./icon/help.png")
sHelp.setIcon(sHelpIcon)

vbox.addWidget(sHelp)
sHelp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

sExit = QPushButton('Exit',window)
sExitIcon = QIcon("./icon/exit.png")
sExit.setIcon(sExitIcon)

vbox.addWidget(sExit)
sExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

frameAnimate_1 = QPropertyAnimation(settingFrame , b"geometry")
frameAnimate_1.setDuration(300)
frameAnimate_1.setStartValue(QRect(690 , 0 , 178 , 278))
frameAnimate_1.setEndValue(QRect(509 , 0 , 178 , 278))

frameAnimate_2 = QPropertyAnimation(settingFrame , b"geometry")
frameAnimate_2.setDuration(300)
frameAnimate_2.setStartValue(QRect(509 , 0 , 178 , 278))
frameAnimate_2.setEndValue(QRect(690 , 0 , 178 , 278))
def setting():
    if gear.x() != 445:
        frameAnimate_1.start()
        gearAnimate_1.start()
    else:
        frameAnimate_2.start()
        gearAnimate_2.start()


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
""")

def help(self):
    import help

sHelp.clicked.connect(help)

def keyboard(self):
    import keyboard

Skeyboard.clicked.connect(keyboard) 

def mouse(self):
   import mouse

sMouse.clicked.connect(mouse)

def media(self):
    import media


sMedia.clicked.connect(media)


def voiceReaco():
    voice.hide()
    import random
    import json

    import torch
    sys.path.insert(0,"../ECHO/code/voice/")
    from MODEL import NeuralNet
    from NLTK import bag_of_words, tokenize

    import OPEN as op
    import pyttsx3
    import HEAR_SPEAK as hsk

    engine=pyttsx3.init()

    SEARCH_WORDS=op.SEARCH_WORDS
    def speak(word):
        title.setText(word) ##############
        engine.setProperty('rate', 135)
        engine.setProperty('volume', 1)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
        engine.say(str(word))
        engine.runAndWait()
        engine.stop()


    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open("../ECHO/code/voice/final_intent.json", 'r') as json_data:
        intents = json.load(json_data)

    FILE = "../ECHO/code/voice/data.pth"
    data = torch.load(FILE,map_location=torch.device('cpu'))

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    bot_name = "Echo"
    ##print
    title.setText("Let's chat! (type 'quit' to exit)")
    while True:
        
        try:
            sentence = hsk.start()
            sentence = str(sentence)
            title.setText(sentence)
            #print(sentence)
            if 'search' in sentence:
                #print ("do you want to search in your device or on google")
                #title.setText("do you want to search in your device or on google")
                speak("do you want to search in your pc or on google")
                inp = str(op.rec_audio())
                if 'desktop' in inp or 'device':
                    print(op.file())
                else :
                    ser= str(op.rec_audio())
                    op.search(ser)
                    
                sentence = hsk.start()
                sentence = str(sentence)
                title.setText(sentence)
            elif sentence == "quit":
                break
            ser_word=sentence
            
            sentence = tokenize(sentence)
            X = bag_of_words(sentence, all_words)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X).to(device)

            output = model(X)
            _, predicted = torch.max(output, dim=1)

            tag = tags[predicted.item()]

            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]
            if prob.item() > 0.95:
                for intent in intents['intents']:
                    if tag == intent["tag"]:
                        if intent["tag"]=='open_google':
                            op.open_google()
                        elif  intent["tag"]=="open_youtube":
                            op.open_youtube()
                        elif  intent["tag"]=="today":
                            res=op.today()
                            speak(res)
                            print (res)
                        elif intent["tag"]=="time":
                            res=op.time()
                            speak(res)
                            print (res)
                        elif  intent["tag"]=="yesterday":
                            res=op.yesterday()
                            speak(res)
                            print (res)
                        elif  intent["tag"]=="last_year":
                            res=op.last_year()
                            speak(res)
                            print (res)
                        elif  intent["tag"]=="last_week":
                            res=op.last_week()
                            speak(res)
                            print (res)
                        elif  intent["tag"]=="weather":
                            res=op.weather()
                            speak(res)
                            print (res)
                        elif  intent["tag"]=="email":
                            op.e_mail()
                        elif  intent["tag"]=="note":
                            op.make_note()
                        elif  intent["tag"]=="virtual_mouse":
                            op.virtual_mouse()
                        elif  intent["tag"]=="virtual_keyboard":
                            op.virtual_keyboard()
                            
                        
                            
                            
                        response=f"{random.choice(intent['responses'])}"
                        if response !="":
                            print(f"{bot_name}:",response)
                            speak(response)
                            
            
            else:
                speak('I really dont know that well, so i tried to find it for you')
                speak(op.search(str(ser_word).lower()))
                
        except:
           #print("may be something wrong happened")
           speak("may be something wrong happened")           

thread =QThread()
from PyQt5.QtCore import QThreadPool
def gg():
   pool = QThreadPool.globalInstance()
   pool.start(voiceReaco)
voice.clicked.connect(gg)

gear.clicked.connect(setting)
sExit.clicked.connect(QApplication.instance().quit)
window.show()
app.exec_()