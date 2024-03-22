import speech_recognition as sr
import os


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(
            source, 0, 8
        )  # Jasrvis gets stuck in listening mode, so the 8 is to specify that if cuts the listening after every 8 seconds

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except:
        return ""

    query = str(query).lower()
    print(query)
    return query  # Prints in hindi


def wakeupDetected():
    query = Listen().lower()

    if "wake up" in query:
        print("waking")
        os.startfile(r"D:\Codes\JARVIS\Main.py")

    else:
        pass


while True:
    wakeupDetected()
