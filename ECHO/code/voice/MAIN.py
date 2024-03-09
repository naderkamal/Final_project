import random
import json

import torch

from MODEL import NeuralNet
from NLTK import bag_of_words, tokenize

import OPEN as op
import pyttsx3
import HEAR_SPEAK as hsk
textT ="Let's chat! (type 'quit' to exit)"
engine=pyttsx3.init()

SEARCH_WORDS=op.SEARCH_WORDS
def speak(word):
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
print("Let's chat! (type 'quit' to exit)")
while True:
    
    try:
        sentence = hsk.start()
        sentence = str(sentence)
        
        print(sentence)
        if 'search' in sentence:
            print ("do you want to search in your device or on google")
            speak("do you want to search in your pc or on google")
            inp = str(op.rec_audio())
            if 'desktop' in inp or 'device':
                print(op.file())
            else :
                ser= str(op.rec_audio())
                op.search(ser)
                
            sentence = hsk.start()
            sentence = str(sentence)
            
        elif sentence == "quit": ##### EXIT APP
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
        if prob.item() > 0.75:
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
      print("may be something wrong happened")
      speak("may be something wrong happened")           
