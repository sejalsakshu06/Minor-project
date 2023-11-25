import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
import pyttsx3
import speech_recognition as sr
import requests
import pywhatkit
import wikipedia
import os
import subprocess
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
from pyowm import OWM
import requests
import random

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[1].id)
# Set your Spotify API credentials
SPOTIPY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'  # Set this in your Spotify Developer Dashboard

# Initialize Spotify API authentication
sp_oauth = SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope='user-library-read user-read-playback-state user-modify-playback-state')
token_info = sp_oauth.get_cached_token()
# Function to capture voice command
def takecommand():
    microphone = sr.Microphone()
    with microphone as source:
        statement="Listening for a command (online)..."
        print(statement)
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        recognizer.energy_threshold = 4000
    try:
        command = recognizer.recognize_google(audio)
        statement=f"Recognized online command: {command}"
        print(statement)
        return command  # Return the recognized command
    except sr.UnknownValueError:
        statement=Speak("Sorry, I couldn't understand the audio.")
        print(statement)
        return None  # Return None when the command is not understood

# Function to speak a message
def Speak(audio):
    statement = "Assistant: " + audio
    reply_label.config(text=statement)  # Update reply_label with the spoken statement
    print(statement)  # Print the statement

    # Stop the TTS engine if it's already running
    Assistant.stop()

    Assistant.say(audio)  # Speak the message
    Assistant.runAndWait()
    return statement  # Return the spoken statement


def youtube():
    statement=Speak("Tell me the Name of the video")
    print(statement)
    videoName = takecommand()
    pywhatkit.playonyt(videoName)
    statement=Speak("Your video has been Started, Enjoy")
    print(statement)


def get_weather(city_name):
    owm = OWM('3b91764244d706e6dceab2dc46490cb5')  # Replace with your OpenWeatherMap API key
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city_name)
    w = observation.weather

    weather_info = f"The weather in {city_name} is {w.detailed_status}. "
    weather_info += f"The temperature is {w.temperature('celsius')['temp']}°C."

    return weather_info


# Function to get current time
def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."
# Function to fetch a random English joke
def get_english_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        # Add more English jokes as needed
    ]
    joke = random.choice(jokes)
    statement = Speak(joke)
    print(statement)
    return joke



# Function to fetch a random Hindi joke
def get_hindi_joke():
    jokes = [
        "एक दोस्त ने पुच्छा: तेरी गर्लफ्रेंड तेरे साथ कैसे रहती है? \nमैंने कहा: बिलकुल नयी बात है, मैं उसके साथ रहता हूँ!",
        "बच्चा: पप्पा, तुम शादी के लिए कौनसी बाते देखते हो? \nपापा: यही कि कहीं तेरी माँ मुझसे कम उम्र की नहीं हो!",
        "महोब्बत और बंक लूट एक ही बात है,\nबस फर्क इतना है कि\nएक में पैसा लुटते हैं और दूसरे में दिल!\n",
        # Add more Hindi jokes as needed
    ]
    joke = random.choice(jokes)
    statement = Speak(joke)
    print(statement)
    return joke

# Function to play a song on Spotify
def play_spotify_song(track_name):
    sp = spotipy.Spotify(auth=token_info['access_token'])
    results = sp.search(q=track_name, type='track', limit=1)

    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
        Speak(f"Playing {track_name} on Spotify.")
    else:
        Speak(f"Sorry, {track_name} not found on Spotify.")

def YoutubeAuto():
    Speak("What's your command?")
    query = takecommand()
    if 'restart' in query:
        os.system("0")
    elif 'mute' in query:
        os.system("m")
    elif 'skip' in query:
        os.system("l")
    elif 'back' in query:
        os.system("j")
    elif 'full screen' in query:
        os.system("f")
    elif 'film mode' in query:
        os.system("t")
    elif 'pause' in query:
        os.system("k")
    Speak('Done Sir')

def ChromeAuto():
    Speak('Chrome Automation Started!')
    command = takecommand()
    if 'close this tab' in command:
        os.system("TASKKILL /F /im Chrome.exe")
    elif 'open new tab' in command:
        os.system("start chrome.exe --new-tab")
    elif 'open new window' in command:
        os.system("start chrome.exe --new-window")
    elif 'history' in command:
        os.system("start chrome.exe --chrome --new-window chrome://history")


# Replace 'YOUR_NEWS_API_KEY' with the actual API key you obtained from News API
NEWS_API_KEY = 'c099a32bdc704307a93c846fc0edbf06'


# Function to get today's news headlines
def get_news():
    news_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'  # Adjust the country code if needed
    response = requests.get(news_url)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']

        if articles:
            news_info = "Here are today's headlines:\n"
            for idx, article in enumerate(articles):
                news_info += f"{idx + 1}. {article['title']}\n"
            return news_info
        else:
            return "Sorry, I couldn't fetch the latest news at the moment."
    else:
        return "Sorry, I couldn't fetch the latest news at the moment."
def youtubeSearch(query):
    query = query.replace("VIRTIGO", "")
    query = query.replace("youtube search", "")
    web = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(web)
    Speak("Done Sir!")

# Main function to execute the assistant
def TaskExe():
    try:
        statement = Speak("Hello, I am VERTIGO, your Personal Assistant. How may I help you?")
        print(statement)

        try:
            # Check if the internet is available by making a simple request
            response = requests.get("https://www.google.com")
        except requests.ConnectionError:
            statement = Speak("Please check your internet connection. Sorry for the inconvenience.")
            print(statement)  # Print the spoken statement

        while True:
            query = takecommand()

            if query is not None:
                if 'hello' in query:
                    statement = Speak("Hello! bolo kya kaam hai")
                    print(statement)
                elif 'hey' in query:
                    statement = Speak("Hey! How can I assist you?")
                    print(statement)
                elif 'hii' in query:
                    statement = Speak("hii! How can I assist you?")
                    print(statement)
                    break
                elif 'exit' in query or 'bye' in query or 'dfa ho' in query:
                    statement = Speak("byee have a nice day")
                    print(statement)
                    break
                elif 'how are you' in query:
                    statement = Speak("I am fine, sir. What about you?")
                    print(statement)
                elif 'weather' in query:
                    city_name = "Solan"  # Replace with your desired city
                    weather_info = get_weather(city_name)
                    statement = Speak(weather_info)
                    print(statement)
                elif 'time' in query:
                    time_info = get_current_time()
                    statement = Speak(time_info)
                    print(statement)
                elif 'news' in query:
                    news_info = get_news()
                    statement = Speak(news_info)
                    print(statement)
                elif 'joke' in query:
                    if 'Hindi' in query:
                        joke_info = get_hindi_joke()
                        statement = Speak(joke_info)
                        print(statement)
                    else:
                        joke_info = get_english_joke()
                    statement = Speak(joke_info)
                    print(statement)

                elif 'you need a break' in query:
                    statement = Speak("Okay, sir. You can call me anytime.")
                    print(statement)
                    break
                elif 'kya hal hai' in query:
                    statement = Speak("Main badiya hoon, ap batao.")
                    print(statement)
                elif 'youtube search' in query:
                    statement = Speak("Okay, this is what I found")
                    print(statement)
                    youtubeSearch(query)
                    break
                elif 'news' in query:
                    news_info = get_news()
                    statement = Speak(news_info)
                    print(statement)
                elif 'Google search' in query:
                    Speak("This is what I found for your search")
                    query = query.replace("jarvis", "").replace("google search", "")
                    pywhatkit.search(query)
                    Speak("Done Sir!")
                elif 'website' in query:
                    Speak("Ok Sir, Launching.....")
                    query = query.replace("jarvis", "").replace("website", "").replace("open", "")
                    web2 = 'https://www.' + query + '.com'
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
                elif 'play music' in query:
                    statement = Speak("Tell me the name of the song.")
                    print(statement)
                    music_name = takecommand()
                    play_spotify_song(music_name)
                elif 'play youtube video' in query:
                    youtube()

                elif 'Wikipedia' in query:
                    Speak("searching wikipedia.....")
                    query = query.replace("jarvis", "")
                    query = query.replace("wikipedia", "")
                    wiki = wikipedia.summary(query, 2)
                    Speak("According to wikipedia:" + wiki)


                elif 'Chrome' in query:
                    subprocess.run("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                elif 'Edge' in query:
                    subprocess.run("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                elif 'control panel' in query:
                    subprocess.run(
                        "C:\\Users\\sejal\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
                elif 'Command prompt' in query:
                    subprocess.run(
                        "C:\\Users\\sejal\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
                elif 'Facebook' in query:
                    webbrowser.open('https://www.facebook.com/login/')
                elif 'Instagram' in query:
                    webbrowser.open('https://www.instagram.com/accounts/login/')
                elif 'Linkedin' in query:
                    webbrowser.open('https://www.linkedin.com')
                elif 'netflix' in query:
                    webbrowser.open('https://www.netflix.com/login/')
                elif 'netflix' in query:
                    webbrowser.open('https://www.netflix.com/login/')
                elif 'pause' in query or 'restart' in query or 'mute' in query or 'volume up' in query or 'volume down' in query or 'skip' in query or 'back' in query or 'full screen' in query or 'film mode' in query or 'pause' in query:
                    os.system('pause')
                elif 'youtube tool' in query:
                    YoutubeAuto()
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        Speak("Your network is quite slow try again bye")

# Create a Tkinter window
window = tk.Tk()
window.title("Vertigo Assistant")  # Set the window title

# Load the initial GIF
gif_path = "X:\\python project\\vertigo.gif"
gif = Image.open(gif_path)

# Convert the GIF to a sequence of PhotoImage objects
photo_sequence = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

# Function to update the GIF displayed
def update_gif(index):
    label.configure(image=photo_sequence[index])
    window.after(100, update_gif, (index + 1) % len(photo_sequence))

# Create a label to display the GIF
label = tk.Label(window)
label.pack()

# Create a label to display the assistant's reply
reply_label = tk.Label(window, text="")
reply_label.pack()

# Start the animation with the initial GIF
window.after(0, update_gif, 0)

# Create a button in the Tkinter window
button = tk.Button(window, text="Start Assistant", command=lambda: threading.Thread(target=TaskExe).start())
button.pack()

# Function to handle window closing
def on_close():
    window.destroy()

# Set the close event handler for the window
window.protocol("WM_DELETE_WINDOW", on_close)

# Run the Tkinter event loop
window.mainloop()
