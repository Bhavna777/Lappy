import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice', voices[1])

### to take a voice form system (start) ###

def speak(audio):
    engine = pyttsx3.init() 
    engine.say(audio)
    engine.runAndWait()

### to take a voice form system (end) ###


### this function is used here to wish me good morning, good afternoon, good evening (start) ### 

def wishMe():
    speak("Hello Bhavna")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I'm Lappy your cute friend please tell me how can I help you?")
### this function is used here to wish me good morning, good afternoon, good evening (end) ###


### this function is used hare to recognize my voice (start) ###

def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recongnizing...")
            query = r.recognize_google(audio)
            print(f"User Said : {query}\n")

        except Exception as e:
            # print(e)
            print("Please try again")
            return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open free code camp' in query:
            webbrowser.open("freecodecamp.com")
        elif 'play song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=qfdShSZZxlg")
        else:
            exit()

