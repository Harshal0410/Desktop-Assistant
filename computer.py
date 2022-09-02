import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 or hour < 12:
        speak("Good Morning!")
    elif hour >= 12 or hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am computer. How may I help you!")

def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
    
if __name__ == "__main__":
    wishMe()
    while(True):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query  = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            # speak("Opening Youtube")
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open_new('https://www.google.com/')

        elif 'open stack overflow' in query:
            webbrowser.open_new('https://stackoverflow.com/')
            
        elif 'play music' in query:
            speak("Playing song")
            music = "D:\\music"
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[random.randint(0,len(songs))]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'computer quit' in query:
            exit()