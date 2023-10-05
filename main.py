import pyttsx3 #install "pip install pyttsx3"
import speech_recognition as sr#install "pip install speechrecoognition"

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[1].id)
def  Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(" ")
    Assistant.runAndWait()
def takecommand():
    command=sr.Recognizer()
    with (sr.Microphone() as source):
        print("listening....")
        command.pause_threshold=1
        audio = command.listen(source)

        try:
            print("recognizing....")
            query= command.recognize_google(audio,language='en-in')
            print(f"you said : {query}")
        except Exception as Error:
            return "none"
        return query.lower()

query = takecommand()

def TaskExe():

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello sir,I am jarvis")
            Speak("You Personal AI Assistant")
            Speak("How may I help You")
        elif 'how are you' in query:
            Speak("I am fine sir")
            Speak("What about you")
        elif 'you need a break' in query:
            Speak("Ok sir,you can call me anytime")
            break
        elif 'kya haal hai' in query:
            Speak("Main Badiya hoon app btao")

        elif 'bye' in query:
            Speak("Ok sir,bye!")
            break

TaskExe()
