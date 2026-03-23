ASSISTANT_NAME = "Nova"
import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import os
import datetime
import webbrowser
pygame.mixer.init()
def speak(text):
    print("Assistant:", text)
    tts = gTTS(text=text, lang='en')
    tts.save("voice.mp3")
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.unload()
    os.remove("voice.mp3")
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""
    speak(f"Hello, I am {ASSISTANT_NAME}, your voice assistant")
while True:
    command = listen()
    if command == "":
        speak("Please say that again")
        continue
    elif "hello" in command or "hi" in command:
        speak("Hello! Nice to meet you")
    elif "who are you" in command:
        speak(f"I am {ASSISTANT_NAME}, your voice assistant")
    elif "how are you" in command:
        speak("I am great, what about you")
    elif "i am fine" in command or "i am good" in command:
        speak("That's nice to hear")
    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {date}")
    elif "search" in command:
        speak("What should I search?")
        query = listen()
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "open youtube" in command:
        os.system("start https://www.youtube.com")
    elif "open google" in command:
        os.system("start https://www.google.com")
    elif "open notepad" in command:
        os.system("notepad")
    elif "open calculator" in command:
        os.system("calc")
    else:
        speak("I did not understand that")