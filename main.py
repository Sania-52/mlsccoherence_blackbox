import speech_recognition as sr
import pyttsx3

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except Exception as e:
        print(e)
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def jarvis():
    speak("Hello customer, I am your Virtual Assistant. How can I assist you today?")
    while True:
        query = listen()
        if "hello" in query:
            speak("Hi, how can I help you?")
        elif "bye" in query:
            speak ("Goodbye. Have a great day.")
            break
        elif "have an issue" in query:
            speak("Sorry to hear that, please be assured that your problem will be resolved. Please elaborate.")
        elif "laptop is crashing" in query:
            speak("Try Restarting, if that does not work we can help you contact the IT department on 770935366")
        elif "keypad is not working" in query:
            speak("That's unfortunate. We can schedule your appointment to the nearest service center")   
        else:
            speak("Sorry, I didn't understand. Can you please repeat or ask something else?")

if __name__ == "_main_":
    jarvis()
