import speech_recognition as sr
import webbrowser
import pyttsx3
import sounddevice as sd
import numpy as np   
import time
import musiclibrary

recognizer = sr.Recognizer()

def speak(text):          
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  

def processcommand(c):
    c = c.lower()

    if c.startswith("stop"):
       speak("stopping boss")
       return

    if c.startswith("open"):
        app = " ".join(c.split(" ")[1:])
        if app in musiclibrary.apps:
            webbrowser.open(musiclibrary.apps[app])
        else:
            speak(f"sorry boss, I don't know {app}")

    elif c.startswith("play"):
        song = " ".join(c.split(" ")[2:])
        if song in musiclibrary.music:
            webbrowser.open(musiclibrary.music[song])
        else:
            speak(f"sorry boss, song {song} not found")

    elif c.startswith("play movie"):
        movie = " ".join(c.split(" ")[2:])
        if movie in musiclibrary.movies:
            webbrowser.open(musiclibrary.movies[movie])
        else:
            speak(f"sorry boss, movie {movie} not found")

    elif c.startswith("play show"):
        show = " ".join(c.split(" ")[2:])
        if show in musiclibrary.shows:
            webbrowser.open(musiclibrary.shows[show])
        else:
            speak(f"sorry boss, show {show} not found")

    elif c.startswith("search"):
        query = " ".join(c.split(" ")[1:])
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "time" in c:
        t = time.strftime("%I:%M %p")
        speak(f"boss, the time is {t}")

    elif "date" in c:
        d = time.strftime("%d %B %Y")
        speak(f"boss, today is {d}")

    else:
        speak("sorry boss, I did not understand the command")   


             

if __name__ == "__main__":
    speak("initializing kavya.......")
    
    while True:
        r = sr.Recognizer()
        print("listening.....")
        
        fs = 16000  
        seconds = 3
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')  
        sd.wait()

        audio_bytes = recording.tobytes()  
        audio = sr.AudioData(audio_bytes, fs, 2)

        print("recognizing......")
        try:
            word = r.recognize_google(audio)
            print("You said:", word)

            if "kavya" in word.lower().strip():
               print("MATCHED")
               speak("yeah boss")
               time.sleep(1)
               
               print("listening for command...")
               recording2 = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
               sd.wait()
               audio_bytes2 = recording2.tobytes()
               audio2 = sr.AudioData(audio_bytes2, fs, 2)
               command = r.recognize_google(audio2)
               print("Command:", command)
               processcommand(command)  
        except Exception as e:
            print("error: {0}".format(e))



           