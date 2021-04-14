import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import pyautogui
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    #speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        print(f"Good Morning Yash, its {tt}")
        speak(f"Good Morning Yash, its {tt}")

    elif hour >= 12 and hour < 18:
        print(f"Good Afternoon Yash, its {tt}")
        speak(f"Good Afternoon Yash, its {tt}")

    else:
        speak("good evening sir")

    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='eng-in')
        print(f"Yash Said: {query}\n")
    
    except Exception as e:
        speak("sir please say that again")
        print("Say That Again")
        return "None"
    return query



#if __name__ == '__main__':
def TaskExecution():
    #startup()
    wish()
    takecommand()
    
    while True:

        query = takecommand().lower()

        # to find something on wikipedia  

        if "wikipedia" in query:
            speak("I am finding on wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "search on google" in query:
            speak("sir what you want to search on google")
            search = takecommand().lower()
            webbrowser.open(f"{search}")

        elif "play music" in query:
            music_dir = 'E:\\Yash Iphone\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif "play some song to focus" in query:
            speak("sir what you want to play")

            if "which song tony stark like most" in condition:
                music_dir = 'E:\\Jarvis\\Tony Stark Fav Song'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[1]))

        elif "take a screenshot" in query:
            
            speak("sir, please tell me name for this screenshot file")
            name = takeCommand().lower()
            speak("please hold the screen for few seconds i am taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.jpg")
            speak("i am done sir, the screenshot is saved to our main folder now i am ready to take next command")



if __name__ == '__main__':
    TaskExecution()