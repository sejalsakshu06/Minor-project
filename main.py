import pyttsx3 #instll it
import speech_recognition as sr#instll it
import requests#instll it

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

    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized online command: {command}")
        return command  # Return the recognized command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None  # Return None when the command is not understood
    except sr.RequestError as e:
        print(f"Couldn't request results online; {e}")
        return None  # Return None for request errors


# Function to speak a message
def Speak(audio):
    print("Assistant: " + audio)  # Print the message
    Assistant.say(audio)  # Speak the message
    Assistant.runAndWait()


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
                Speak("Hello! How can I assist you?")
            elif 'how are you' in query:
                Speak("I am fine, sir. What about you?")
            elif 'you need a break' in query:
                Speak("Okay, sir. You can call me anytime.")
                break
            elif 'kya hal hai' in query:
                Speak("Main badiya hoon, ap batao.")
            elif 'bye' in query:
                Speak("Okay, sir, goodbye!")
                break
            elif 'exit' in query:  # Add an exit command
                Speak("Goodbye!")
                break


# Run the main function
if __name__ == "__main__":
    TaskExe()
