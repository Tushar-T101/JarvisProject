import sys
custom_dir = r"Lib\site-packages"
sys.path.append(custom_dir)

import speech_recognition as sr
from mtranslate import translate
import threading
import os

def translation_hin_to_eng(text):
    english_translation = translate(text, 'en-in')
    return english_translation

def print_loop():
    while True:
        print("Listening....", end='', flush=False)
        print("", end='')

def Listen():
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 35000
    recognizer.dynamic_energy_threshold = True
    recognizer.dynamic_energy_adjustment_damping = 0.1
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.pause_threshold = 0.5
    recognizer.operation_timeout = None
    recognizer.phrase_threshold = 0.2
    recognizer.non_speaking_duration = 0.3

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Please wait. Calibrating microphone...\n")
        while True:
            print("Listening....", end='', flush=False)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + "Recognizing...   ", end='', flush=False)
                recognized_text = recognizer.recognize_google(audio).lower()
                if recognized_text:
                    translated_text = translation_hin_to_eng(recognized_text)
                    print("\r" + "You: " + translated_text)
                else:
                    print("\r" + "Could not understand")
            except sr.UnknownValueError:
                print("\r" + "Sorry, didn't catch you")
            finally:
                print("\r", end='', flush=False)
                os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    Listen()
