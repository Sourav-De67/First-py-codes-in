# ============================================
# VOICE JARVIS - BEGINNER VERSION
# Windows + VS Code
# ============================================

import os
import webbrowser
import datetime
import random
import speech_recognition as sr

# ============================================
# SPEAK FUNCTION
# ============================================

def speak(text):

    print(f"\nJarvis: {text}\n")

# ============================================
# LISTEN FUNCTION
# ============================================

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print(f"You: {command}")

        return command.lower()

    except:

        return ""

# ============================================
# WELCOME
# ============================================

def welcome():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning Sir")

    elif hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("Voice Jarvis Online")

# ============================================
# START
# ============================================

welcome()

while True:

    command = listen()

    # ========================================
    # EXIT
    # ========================================

    if "exit" in command:

        speak("Shutting Down")

        break

    # ========================================
    # TIME
    # ========================================

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

    # ========================================
    # DATE
    # ========================================

    elif "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")

        speak(today)

    # ========================================
    # OPEN GOOGLE
    # ========================================

    elif "open google" in command:

        webbrowser.open("https://google.com")

        speak("Opening Google")

    # ========================================
    # OPEN YOUTUBE
    # ========================================

    elif "open youtube" in command:

        webbrowser.open("https://youtube.com")

        speak("Opening YouTube")

    # ========================================
    # OPEN CHATGPT
    # ========================================

    elif "open chatgpt" in command:

        webbrowser.open("https://chat.openai.com")

        speak("Opening ChatGPT")

    # ========================================
    # OPEN NOTEPAD
    # ========================================

    elif "open notepad" in command:

        os.system("notepad")

        speak("Opening Notepad")

    # ========================================
    # OPEN CALCULATOR
    # ========================================

    elif "open calculator" in command:

        os.system("calc")

        speak("Opening Calculator")

    # ========================================
    # OPEN CMD
    # ========================================

    elif "open cmd" in command:

        os.system("start cmd")

        speak("Opening Command Prompt")

    # ========================================
    # SEARCH GOOGLE
    # ========================================

    elif "search" in command:

        query = command.replace("search", "")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        speak(f"Searching for {query}")

    # ========================================
    # PLAY MUSIC
    # ========================================

    elif "play" in command:

        song = command.replace("play", "")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={song}"
        )

        speak(f"Playing {song}")

    # ========================================
    # JOKES
    # ========================================

    elif "joke" in command:

        jokes = [

            "Why do programmers hate nature? Too many bugs.",

            "Why was the computer cold? Because it left its Windows open.",

            "Why did Python live on land? Because it was above C level."
        ]

        speak(random.choice(jokes))

    # ========================================
    # SHUTDOWN
    # ========================================

    elif "shutdown" in command:

        speak("Shutting down system")

        os.system("shutdown /s /t 5")

    # ========================================
    # RESTART
    # ========================================

    elif "restart" in command:

        speak("Restarting system")

        os.system("shutdown /r /t 5")

    # ========================================
    # LOCK PC
    # ========================================

    elif "lock pc" in command:

        speak("Locking PC")

        os.system(
            "rundll32.exe user32.dll,LockWorkStation"
        )

    # ========================================
    # UNKNOWN COMMAND
    # ========================================

    else:

        speak("Command not recognized")