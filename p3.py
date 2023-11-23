from distutils.cmd import Command
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechrecognition
import requests  # pip install requests
import turtle  # pip install turtle
import webbrowser  # pip install webbrowser
import pywhatkit  # pip install pywhatkit
import wikipedia  # pip install wikipedia
import os
import pyautogui  # pip install pyautogui
import keyboard  # pip install keyboard
import subprocess

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[1].id)


# Function to capture voice command
def takecommand():
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for a command (online)...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        recognizer.energy_threshold = 4000
    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized online command: {command}")
        return command  # Return the recognized command
    except sr.UnknownValueError:
        Speak("Sorry, I couldn't understand the audio.")

        return None  # Return None when the command is not understood


# Function to speak a message
def Speak(audio):
    print("Assistant: " + audio)  # Print the message
    Assistant.say(audio)  # Speak the message
    Assistant.runAndWait()


def Music():
    Speak("Tell me the Name of the Song")
    musicName = takecommand()
    pywhatkit.playonyt(musicName)
    Speak("Your song has been Started,Enjoy")



def WhatsApp():
    Speak("Tell me the name of person")
    name = takecommand()

    if 'Mumma' in name:
        Speak("Tell me the mesage!")
        msg = takecommand()
        Speak("Tell me the Time Sir")
        Speak("Time in Hour")
        hour = int(takecommand())
        Speak("Time in Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+917876757577", msg, hour, min, 20)
        Speak("OK Sir , Sending Whatsapp Message !")

    elif 'Cutu' in name:
        Speak("Tell me the mesage!")
        msg = takecommand()
        Speak("Tell me the Time Sir")
        Speak("Time in Hour")
        hour = int(takecommand())
        Speak("Time in Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+918219424243", msg, hour, min, 20)
        Speak("OK Sir , Sending Whatsapp Message !")

    elif 'papa' in name:
        Speak("Tell me the mesage!")
        msg = takecommand()
        Speak("Tell me the Time Sir")
        Speak("Time in Hour")
        hour = int(takecommand())
        Speak("Time in Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+919805662339", msg, hour, min, 20)
        Speak("OK Sir , Sending Whatsapp Message !")

    else:
        Speak("Tell me the Phone Number!")
        phone = int(takecommand())
        ph = '+91' + str(phone)
        msg = takecommand()
        Speak("Tell me the Time Sir")
        Speak("Time in Hour")
        hour = int(takecommand())
        Speak("Time in Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
        Speak("OK Sir , Sending Whatsapp Message !")


def OpenApps():
    Speak('OK Sir, Wait a second!')
    query = takecommand()

    if query is not None:
        if 'Chrome' in query:
            subprocess.run("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        elif 'Edge' in query:
            os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        elif 'Facebook' in query:
            webbrowser.open('https://www.facebook.com/login/')
        elif 'Instagram' in query:
            webbrowser.open('https://www.instagram.com/accounts/login/')

        Speak("Your command has been successfully completed")
    else:
        Speak("Sorry, I couldn't understand your command.")


def CloseApps():
    Speak("OK Sir,Wait a Second!")
    query = takecommand()
    if 'Instagram' in query:
        os.system("TASKKILL /F /im Chrome.exe")

    elif 'Facebook' in query:
        os.system("TASKKILL /F /im Chrome.exe")

    elif 'Edge' in query:
        os.system("TASKKILL /F /im Edge.exe")

    elif 'Chrome' in query:
        os.system("TASKKILL /F /im Chrome.exe")


def YoutubeAuto():
    Speak("What's your command?")
    query = takecommand()

    if 'restart' in query:
        keyboard.press('0')

    elif 'mute' in query:
        keyboard.press('m')

    elif 'skip' in query:
        keyboard.press('l')

    elif 'back' in query:
        keyboard.press('j')

    elif 'full screen' in query:
        keyboard.press('f')

    elif 'film mode' in query:
        keyboard.press('t')

    elif 'pause' in query:
        keyboard.press('k')

    Speak('Done Sir')


def ChromeAuto():
    Speak('Chrome Automation Started!')

    command = takecommand()

    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')

    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')

    elif 'history' in command:
        keyboard.press_and_release('ctrl + h')


def youtubeSearch(query):
    query = query.replace("VIRTIGO", "")
    query = query.replace("youtube search", "")
    web = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(web)
    Speak("Done Sir!")


# Main function to execute the assistant
def TaskExe():
    Speak("Hello, I am VERTIGO, your Personal Assistant. How may I help you?")

    try:
        # Check if the internet is available by making a simple request
        response = requests.get("https://www.google.com")
    except requests.ConnectionError:
        Speak("Please check your internet connection. Sorry for the inconvenience.")
        return

    while True:
        query = takecommand()

        if query is not None:
            if 'hello' in query:
                Speak("Hello! bolo kya kaam hai")

            elif 'hey' in query:
                Speak("Hey! How can I assist you?")

            elif 'Hii' in query:
                Speak("hii!How can I assist you?")
                break

            elif 'how are you' in query:
                Speak("I am fine, sir. What about you?")

            elif 'you need a break' in query:
                Speak("Okay, sir. You can call me anytime.")
                break

            elif 'kya hal hai' in query:
                Speak("Main badiya hoon, ap batao.")



            elif 'youtube search' in query:
                Speak("Okay this is what i found")
                youtubeSearch(query)
                break

            elif 'google search' in query:
                Speak("This is what i found for your search")
                query = query.replace("jarvis", "")
                query = query.replace("google search", "")
                pywhatkit.search(query)
                Speak("Done Sir!")

            elif 'website' in query:
                Speak("Ok Sir,Launching.....")
                query = query.replace("jarvis", "")
                query = query.replace("website", "")
                web1 = query.replace("open", "")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched")

            elif 'launch' in query:
                Speak("Tell me the name of the website!")
                name = takecommand()
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                Speak("Done sir")

            elif 'facebook' in query:
                Speak("ok sir!")
                webbrowser.open("https://www.facebook.com")
                Speak("Done Sir!")

            elif 'music' in query:
                Music()

            elif 'Wikipedia' in query:
                Speak("searching wikipedia.....")
                query = query.replace("jarvis", "")
                query = query.replace("wikipedia", "")
                wiki = wikipedia.summary(query, 2)
                Speak("According to wikipedia:" + wiki)

            elif 'WhatsApp message' in query:
                print("insider the if conodotioooon")
                WhatsApp()


            elif 'open Chrome' in query:
                subprocess.run("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            elif 'open edge' in query:
                subprocess.run(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

            elif 'open Facebook' in query:
                OpenApps()

            elif 'open Instagram' in query:
                OpenApps()

            elif 'close Chrome' in query:
                CloseApps()

            elif 'close Edge' in query:
                CloseApps()

            elif 'close Facebook' in query:
                CloseApps()

            elif 'close Instagram' in query:
                CloseApps()

            elif 'pause' in query:
                keyboard.press('space bar')

            elif 'restart' in query:
                keyboard.press('0')

            elif 'mute' in query:
                keyboard.press('m')

            elif 'skip' in query:
                keyboard.press('l')

            elif 'back' in query:
                keyboard.press('j')

            elif 'full screen' in query:
                keyboard.press('f')

            elif 'film mode' in query:
                keyboard.press('t')

            elif 'pause' in query:
                keyboard.press('k')

            elif 'youtube tool' in query:
                YoutubeAuto()

            elif 'close this tab' in query:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in query:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in query:
                keyboard.press_and_release('ctrl + h')

            elif 'chrome automation' in query:
                ChromeAuto()


TaskExe()
# takecommand()
