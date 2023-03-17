import openai as oa

import json

#import for speech_recognition
from cgitb import text
import pyttsx3
import datetime as time
import speech_recognition as sr

#code for speech_recognition
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print("the available voices are :")
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish me function which greets the user according to the current time
def wishMe():
    hour = int(time.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")
    else:
        speak("Good Evening sir!")
    speak("I am Jarvis sir , Please tell me how may i help you")



# takecommand function takes input from the user in the form of voice through the microphone and responds
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.record(source,duration=10)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio,language='en-in')
        print(f"User said: {text}\n")
        speak("Your question is"+text)

    except Exception as e:
        print(e)
        print("could you please repeat that again sir...")
        return "None"
    return text

# code for chatGPT API
def apicall():
    try:
        oa.api_key = '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'
        model_engine ='text-davinci-003'
        # prompt = str(input())
        prompt = json.dumps(takeCommand())
        completion = oa.Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.5)
        response =completion.choices[0].text
        print(response)
        speak(response)

    except Exception as e:
        print(e)
        # speak(e)

# the main function to call the functions 
if __name__=="__main__":
    wishMe()
    # takeCommand()
    apicall()