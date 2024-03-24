import speech_recognition as sr
import pyttsx3
import sqlite3

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('jarvis.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY,
                    query TEXT,
                    response TEXT
                )''')
    conn.commit()
    conn.close()

# Function to insert an interaction into the database
def log_interaction(query, response):
    conn = sqlite3.connect('jarvis.db')
    c = conn.cursor()
    c.execute('''INSERT INTO interactions (query, response) VALUES (?, ?)''', (query, response))
    conn.commit()
    conn.close()

# Function to retrieve the last interaction from the database
def get_last_interaction():
    conn = sqlite3.connect('jarvis.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM interactions ORDER BY id DESC LIMIT 1''')
    last_interaction = c.fetchone()
    conn.close()
    return last_interaction

# Function to listen to user input
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

# Function to speak a response
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to interact with the user
def jarvis():
    init_db()
    speak("Hello, I am your virtual assistant. How can I assist you today?")
    while True:
        query = listen()
        log_interaction(query, "")
        last_interaction = get_last_interaction()
        if "hello" in query:
            response = "Hi, how can I help you?"
            log_interaction(query, response)
            speak(response)
        elif "bye" in query:
            response = "Goodbye! Have a great day!"
            log_interaction(query, response)
            speak(response)
            break
        elif "how are you" in query:
            response = "I am fine, thank you!"
            log_interaction(query, response)
            speak(response)
        else:
            response = "Sorry, I didn't understand. Can you please repeat or ask something else?"
            log_interaction(query, response)
            speak(response)

if _name_ == "_main_":
    jarvis()
