import webbrowser as wb
from datetime import date, timedelta, datetime
import pyowm
import speech_recognition as sr
import pyttsx3
import smtplib
import ssl
from email.message import EmailMessage
import subprocess
import email_prop as emp
import os
import re
import win32api

engine=pyttsx3.init()
email_sender = emp.email_sender
email_password = emp.email_password

SEARCH_WORDS = {"search":"search","who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "how": "how"}
def speak(word):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 1)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()
def open_google():
    try:
        link = "https://www.google.com"
        wb.open(link)
    except:
        return("sorry cant open at the moment")
       
def open_youtube():
    try:
        link = "https://www.youtube.com"
        wb.open(link)
    except:
         return("sorry cant open at the moment")
     
def today():
    try:
        today = date.today()
        return("Today is " + today.strftime("%B") + " " + today.strftime("%d") + ", " + today.strftime("%Y"))
    except:
        return("maybe something went wrong try again later")
    
def time ():
    try:
         now = datetime.now()
         return("It is " + now.strftime("%I") + now.strftime("%M") + now.strftime("%p") + ".")
    except:
         return("maybe something went wrong try again later")
     
def yesterday():
    try:
         today = date.today()
         date_intent = today - timedelta(days=1)
         return date_intent
    except:
         return("maybe something went wrong try again later")
 
def last_year():
    try:
        today = date.today()
        current_year = today.year

        if current_year % 4 == 0:
            days_in_current_year = 366

        else:
            days_in_current_year = 365
        date_intent = today - timedelta(days=days_in_current_year)
        return date_intent
    except:
        return("maybe something went wrong try again later")

def last_week():
    try:
         today = date.today()
         date_intent = today - timedelta(days=7)
         return date_intent
    except:
         return("maybe something went wrong try again later")

def weather ():
    try:
        OPENWEATHER = emp.open_weather
        home = 'cairo'
        owm = pyowm.OWM(OPENWEATHER)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(home)
        w = observation.weather
        temp = w.temperature('celsius')
        status = w.detailed_status
        return("It is currently " + str(int(temp['temp'])) + " degrees and " + status)
    except:
        return("cant get the information now try latter")
    
def search(command):
    
    wb.open("https://www.google.com/search?q={}".format(command))
    return("Here is what I found.")    
def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recog.adjust_for_ambient_noise(source)
        recog.dynamic_energy_threshold = 3000
        recog.pause_threshold = 2
        audio = recog.listen(source, timeout=5.0)
       
        
       

    try:
        command = recog.recognize_google(audio, language='en_gb')
        print("You said: " + command)
        return command.lower()
       
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    



def note(text):
    date = datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

    


def make_note():
    try:
         speak("What would you like me to write down?")
         note_text = rec_audio()
         note(note_text)
         speak("I have made a note of that.")
    except:
        print("please try again")

def e_mail():
    try:
        speak("What should I say in the subject?")
        subject = rec_audio()
        speak("What should I say in the body")
        body = rec_audio()
        speak("whom should i send")
        email_receiver = input("Enter To Adress : ")
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        speak("Email has been sent !")
    except Exception as e:
                    print(e)
                    speak ("I am not able to send this email")
                    
def find_file(root_folder, rex,var=[]):
   
   try:
        for root,dirs,files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                if result:
                    #print(os.path.join(root, f))
                    var.append(os.path.join(root, f))
                    #os.startfile(os.path.join(root, f))
                    break # if you want to find only one
        return var
   except:
         return("this file dont exist")
        
    
       
                
def find_file_in_all_drives(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    m = win32api.GetLogicalDriveStrings().split('\000')[:-1]
    #except c because it take much time to search
    m.remove('C:\\')
    #you can git it back
   # m.append ('C:\\')
    for drive in m:
        find_file( drive, rex )
            
    return find_file( drive, rex )

            

#comment for input    return list of drives
def file ():
    speak("enter the file name ")
    inp =input("what do want to search for : ")
    return find_file_in_all_drives(str(inp))

def run_voice(self):    
    subprocess.Popen(["python", "../ECHO/code/keyboard.py"])          
from PyQt5.QtCore import QThreadPool
def gg():
   pool = QThreadPool.globalInstance()
   pool.start(run_voice)
        
def virtual_mouse():
    subprocess.Popen(["python", "../ECHO/code/mouse.py"])
def virtual_keyboard():
    subprocess.Popen(["python", "../ECHO/code/keyboard.py"])
    
#x=file()
#print(x):JK

