import speech_recognition as sr
import pyttsx3
import os
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

def gather_info():
    speak("May I have your full name, please?")
    name = listen()

    speak("Could you provide your contact number?")
    phone_number = listen()

    speak("What is the make and model of your laptop?")
    laptop_make_model = listen()

    speak("Do you know the model number of your laptop?")
    model_number = listen()

    speak("Is it okay for our engineer to give you a call regarding your issue?")
    permission = listen()

    if "yes" in permission:
        speak("At what date and time are you available for the call?")
        availability = listen()
        return name, phone_number, laptop_make_model, model_number, availability
    else:
        speak("Alright. Your issue will be noted. Have a good day!")
        return name, phone_number, laptop_make_model, model_number, availability

def create_ticket(name, phone_number, laptop_make_model, model_number, availability):
    ticket_info = f"Name: {name}\nPhone Number: {phone_number}\nLaptop Make and Model: {laptop_make_model}\nModel Number: {model_number}\nAvailability for Call: {availability}\n"
    return ticket_info

def jarvis():
    speak("Hello, I am your Virtual Assistant. How can I assist you today?")
    while True:
        query = listen()
        if "hello" in query:
            speak("Hi, how can I help you?")
        elif "bye" in query:
            speak("Goodbye. Have a great day.")
            break
        elif "have an issue" in query:
            speak("Sorry to hear that, please be assured that your problem will be resolved. Please provide me with some information.")
            info = gather_info()
            if info:
                name, phone_number, laptop_make_model, model_number, availability = info
                ticket = create_ticket(name, phone_number, laptop_make_model, model_number, availability)
                speak("Your issue has been noted. A representative will call you at the mentioned time.")
                print("Ticket Details:", ticket)
                try:
                    filename = "ticket.txt"
                    with open(filename, "w") as file:
                        file.write(ticket)
                    print("Ticket created successfully. Information has been stored in", filename)
                except Exception as e:
                    print("Error occurred while saving ticket to file:", e)
        elif "laptop is crashing" in query:
            speak("Try Restarting, if that does not work we can help you contact the IT department on 770935366")
        elif "keypad is not working" in query:
            speak("That's unfortunate. We can schedule your appointment to the nearest service center")   
        else:
            speak("Sorry, I didn't understand. Can you please repeat or ask something else?")

jarvis()
