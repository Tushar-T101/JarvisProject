import sys
custom_dir = "C:\D\Codes\JARVIS_ENV_12\Lib\site-packages"
sys.path.append(custom_dir)

###############################################################
import speech_recognition as sr
import os
from Jarvis import MainExe
from Features.clap import Tester


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
        print("Waking up...")
        MainExe()

    else:
        pass


while True:
    wakeupDetected()


# data = Tester()
# if "True-Mic" == data:
#     from Jarvis import MainExe

#     MainExe()
