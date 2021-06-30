import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
 try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa','')
            print(command)
 except:
    pass
 return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song )
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have submitted a lot of assignment. So, I will definitely go tomorrow with you')
    elif 'are you single' in command:
        talk('No, I have a boyfriend named Kishan')
    elif 'do you love kishan' in command:
        talk('Yes, I love Kishan very much. I can not live without him but kishan do not love me. He loves someone')
    elif 'ratan' in command:
        talk('ratan is a very good boy of Loknayak Jai Prakash Institute Of Technology(LNJPIT), Chhapra.He is the friend of kishan')

run_alexa()