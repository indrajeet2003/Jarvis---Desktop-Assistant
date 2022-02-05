import time
import pyttsx3                  # pip install pyttsx3
import speech_recognition as sr      # pip install speechrecognition
import wikipedia                # pip install wikipedia
import random
import datetime
import webbrowser
import os
import smtplib
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = (datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am Jarvis. Sir, Please tell me how may I help you.")


def takeCommand():
    # It take microphone input from user and returns string output
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
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('2003indrajeet@gmail.com', '9149074149')
    server.sendmail('2003indrajeet@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'who are you' in query or 'what is your name' in query:
            speak("I am Jarvis. I am here to do you help in your work.")

        elif 'you are good' in query or 'you are really good' in query or 'you are doing well' in query:
            speak("Thank You Sir")

        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)

            print("According to wikipedia")
            print(results)

            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')

        elif 'play music' in query:
            music_dir = "E:\\Songs"
            songs = os.listdir(music_dir)
            r = random.randint(0, len(songs)-1)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[r]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'open the vs code' in query or 'open the visual studio code' in query:
            path = "C:\\Users\\Indrajeet\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open the chrome' in query or 'open the google chrome' in query:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'open the brave' in query:
             path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
             os.startfile(path)

        elif 'search on google' in query:
            speak("What should you want search")
            content = takeCommand()
            import webbrowser

            # to search
            list_of_links = []
            for j in search(content, tld="co.in", num=10, stop=10, pause=2):
                list_of_links.append(j)
            webbrowser.open(list_of_links[0])

        # For taking Notes
        elif 'create note' in query:
            speak("What should you want Name of File")
            file_name = takeCommand()

            speak("Say the Text you want to write")
            content = takeCommand()
            try:
                try:
                    os.makedirs("C:\\Users\\Indrajeet\\Documents\\Jarvis\\Notes\\")
                except Exception as e:
                    pass
                with open(f"C:\\Users\\Indrajeet\\Documents\\Jarvis\\Notes\\{file_name}.txt", "w") as f:
                    f.write(content)
            except Exception as e:
                speak("Your file not created")
            else:
                speak("Your note has been successfully created")

        # For Email
        elif 'email to indrajeet' in query:
            try:
                speak("What should you say?")
                content = takeCommand()
                to = "2003indrajeet@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

