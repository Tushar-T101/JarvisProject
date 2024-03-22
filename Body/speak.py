import sys
custom_dir = r"C:\D\Sem 8\Major Project\jarvis_project\Lib\site-packages"
sys.path.append(custom_dir)

import pyttsx3

engine = pyttsx3.init("sapi5")  # sapi5 is windows api to get voices
# engine = pyttsx3.init("nsss") # For MAC

engine.setProperty('rate', 175)

voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def Speak(Text):
    print("")
    print(f"You: {Text}.")
    print("")
    engine.say(Text)
    # engine.save_to_file('')  # in order to track the communication, but slows the process
    engine.runAndWait()


# Speak("Hello Sir. I am listening. Please ask me something. Please ask me something?")

# Speak('''Shahrukh Khan, also known as the "King of Bollywood," is an Indian actor, film producer, and television personality. He has appeared in more than 80 Bollywood films and earned numerous awards for his performances.''')
