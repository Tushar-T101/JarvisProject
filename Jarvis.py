import sys
custom_dir = "C:\D\Sem 8\Major Project\jarvis_project\Lib\site-packages"
sys.path.append(custom_dir)

###########################################################
import traceback
print("\n>> Starting Up Speak Function...\n")
from Body.speak import Speak
from Body.listen import Listen
from Features.clap import Tester
from Brain.AIBrain import ChatGpt
print("\n>> Done\n")

def MainExe():
    Speak("Hello Sir.\nI am JARVIS. Ready for you...")

    try:
        while True:
            Data = Listen()
            Data = str(Data)

            if "exit" in Data.lower():
                Speak("Goodbye! Have a great day.")
                break

            reply = ChatGpt(Data)
            Speak(reply)

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    MainExe()

# print("\n>> Starting Up Speak Function...\n")
# from Body.speak import Speak
# from Body.listen import Listen
# from Features.clap import Tester
# from Brain.AIBrain import ChatGpt
# print("\n>> Done\n")

# def MainExe():
#     Speak("Hello Sir.\nI am JARVIS. Ready for you...")

#     while True:
#         Data = Listen()
#         Data = str(Data)
#         if (
#             "what is" in Data
#             or "where is" in Data
#             or "question" in Data
#             or "answer" in Data
#         ):
#             reply = ChatGpt(Data)

#         else:
#             reply = ChatGpt(Data)
#         Speak(reply)


# def ClapDetect():
#     query = Tester()
#     if "True-Mic" in query:
#         MainExe()
#     else:
#         pass


# ClapDetect()
