from brain.AIBrain import ReplyBrain
from brain.Qna import QuestionsAnswer
from body.listen import MicExecution
from body.Speak import Speak
from features.Clap import Tester
import speech_recognition as sr
import datetime
import os
import webbrowser
from Main import MainTaskExecution

#from Main import MainTaskExecution

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query

def MainExecution():
    Speak("Hello Sir")
    Speak("I'm cube, I'm Ready To Assist You Sir.")


    while True:

        Data = MicExecution()
        Data = str(Data)
        ValueReturn = MainTaskExecution(Data)
        
        if ValueReturn == True:
            pass

        elif len(Data)<10:
            pass
        
        elif "turn on the tv" in Data:
            webbrowser.open("https://blr1.blynk.cloud/external/api/update?token=jly-Pf6taxeZjIZD-NWNUI_rfEWTepFf&v0=1")
            Speak("ok turning on the tv")
        
        elif "turn off the tv" in Data:
            webbrowser.open("https://blr1.blynk.cloud/external/api/update?token=jly-Pf6taxeZjIZD-NWNUI_rfEWTepFf&v0=0")
            Speak("ok turning off the tv")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply)
            
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def WakeupDetected():
    query = Listen().lower()

    if "wake up" in query:
        print("wakeup detected.. ")
        MainExecution()

    else:
        pass

while True:
    #WakeupDetected()
    MainExecution()