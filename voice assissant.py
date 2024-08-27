import speech_recognition as sr
import pyttsx3
import datetime
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()
def speak(text):
    """Function to speak text."""
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the service.")
    return ""

def tell_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M")
    speak(f"The time is {time_str}")

def tell_date():
    today = datetime.date.today()
    date_str = today.strftime("%B %d, %Y")
    speak(f"Today's date is {date_str}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result_div = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')
    if result_div:
        snippet = result_div[0].get_text()
        speak(f"I found something: {snippet}")
    else:
        speak("Sorry, I couldn't find any information.")

def main():
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search" in command:
            query = command.replace("search", "").strip()
            search_web(query)
        elif "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
