import speech_recognition as sr
import pyttsx3
from datetime import date, timedelta, datetime

recognizer = sr.Recognizer()
microphone = sr.Microphone(sample_rate=16000)

CONVERSATION_LOG="Conversation Log.txt"
WAKE ="Echo"
engine=pyttsx3.init()

def speak(word):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 1)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()
class Echo:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine=pyttsx3.init()
    
    def hear(self, recognizer, microphone, response):
        try:
            with microphone as source:
                print("Waiting for command.")
                recognizer.adjust_for_ambient_noise(source)
                #recognizer.dynamic_energy_threshold = 3000
                recognizer.pause_threshold = 2
                audio = recognizer.listen(source, timeout=5.0)
                command = recognizer.recognize_google(audio, language='en_gb')
                E.remember(command)
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")
            
    
            
    def speak(self,word):
        engine.setProperty('rate', 135)
        engine.setProperty('volume', 1)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        engine.say(str(word))
        engine.runAndWait()
        engine.stop()

           
            ## log file
    def start_conversation_log(self):
        today = str(date.today())
        today = today
        with open(CONVERSATION_LOG, "a") as f:
            f.write("Conversation started on: " + today + "\n")
            
    def remember(self, command):
        with open(CONVERSATION_LOG, "a") as f:
            f.write("User: " + command + "\n")
  #######          
    def listen(self, recognizer, microphone):
         while True:
             try:
                 with microphone as source:
                     print("Listening.")
                     recognizer.adjust_for_ambient_noise(source)
                     recognizer.pause_threshold = 2
                     recognizer.dynamic_energy_threshold = 3000
                     audio = recognizer.listen(source, timeout=5.0)
                     responsem = recognizer.recognize_google(audio, language='en_gb')
                     

                     if responsem == WAKE or responsem =="hello" :
                         
                         E.speak("How can I help you?")
                         print("How can I help you?") 
                         return responsem.lower() 

                     else:
                         pass
             except sr.WaitTimeoutError:
                 pass
             except sr.UnknownValueError:
                 pass
             except sr.RequestError:
                 print("Network error.")
       

E = Echo() 
def start():
    E.start_conversation_log()
    while True:
       response = E.listen(recognizer, microphone)
       command = E.hear(recognizer, microphone, response)
       return command ###
