import pyttsx3 #converts text to speech
import speech_recognition as  sr
import webbrowser
import datetime
import pyjokes#gives the jokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognising.....")
            data=recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not Understood")

def speech_to_txt(x):
    engine=pyttsx3.init()#init is a class
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
speech_to_txt("hello welcome to py voice assistant")


if __name__=='__main__':#this splits the program into two

    while True:
        data1=sptext()
        if "your name" in  data1:
            name="my name is aditya"
            speech_to_txt(name)
        elif "old are you" in data1:
            age="My age is 4 years old"
            speech_to_txt(age)
        elif 'time' in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speech_to_txt(time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'whatsapp' in data1:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'joke' in data1:
            joke_1=pyjokes.get_joke(language="hindi",category="neutral")
            speech_to_txt(joke_1)
            print(joke_1)
        elif "exit" in data1:
            speech_to_txt("Thank you")
            break
