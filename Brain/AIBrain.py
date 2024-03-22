import sys
custom_dir = r"C:\D\Sem 8\Major Project\jarvis_project\Lib\site-packages"
sys.path.append(custom_dir)

# from g4f.client import Client
# from time import time as t
# messages = [
#     {"role": "system", "content": "I'm the latest J.A.R.V.I.S. AI, designed by Divyansh Shukla with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
#     {"role": "user", "content": "Open Google Chrome."},
#     {"role": "assistant", "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
#     {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
#     {"role": "system", "content": """```python
#         from Genration_Of_Images import Generate_Images, Show_Image
#         IMGS = Generate_Images(prompt="iron man")
#         print(IMGS)
#         IMGS_TO_SHOW = Show_Image(IMGS)
#         IMGS_TO_SHOW.open(0)
#         IMGS_TO_SHOW.open(1)
#         ```
#         ```python
#         from func.Jukebox.YouTube import MusicPlayer
#         #taks song name and it stats playing music
#         ncs=MusicPlayer("ncs")
#         #any btw 0 - 100
#         ncs.Vol(30)
#         #pause or play
#         ncs.Play()
#         ncs.Pause()
#         #next song
#         ncs.Next()
#         #quit song
#         ncs.Quit()
#      """},
#     {"role": "user", "content": "Jarvis generate a cute cat image using Python."},
#     {"role": "assistant", "content": """```python
#         from Genration_Of_Images import Generate_Images, Show_Image
#         IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
#         IMGS_TO_SHOW = Show_Image(IMGS)
#         IMGS_TO_SHOW.open(0)
#     ```"""},
#     {"role": "user", "content": "Jarvis show me the next image"},
#     {"role": "assistant", "content": """```python
#         IMGS_TO_SHOW.open(1)
#     ```"""},
#     {"role": "user", "content":"Jarvis play neffex cold"},
#     {"role": "assistant", "content":"""```python\nneffex=MusicPlayer("neffex cold song")```"""}
# ]

# def auto_message_deletion():
#     """
#     Automatically deletes old messages if the total length exceeds a threshold.
#     """
#     global messages
#     # Calculate the total length of messages
#     total_length = sum(len(msg["content"]) for msg in messages)
#     # Set a threshold, adjust it as needed
#     threshold = 5500
#     if total_length > threshold:
#         # Remove the oldest message
#         messages.pop(0)

# def ChatGpt(*args, **kwargs):
#     """
#     Main function for interacting with the GPT-4 model.
#     """
#     global messages
#     assert args != ()
#     auto_message_deletion()

#     message = " ".join(args)
#     messages.append({"role": "user", "content": message})

#     client = Client()
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=messages,
#             stream=True,
#         )

#         response_str = ""
#         for chunk in response:
#             content = chunk.choices[0].delta.content
#             if content is not None:
#                 response_str += content

#         if not response_str:
#             print("Empty response received from the API.")
#             return ""

#         print(response_str.encode('utf-8', 'ignore').decode('utf-8'), end="", flush=True)

#         messages.append({"role": "assistant", "content": response_str})
#         return response_str
    
#     except Exception as e:
#         print("Error:", e)
#         return ""


# # ChatGpt("What is the capital of India?")
# ChatGpt("What is the full form of DNA")
# # # # ChatGpt("Explain String theory")
# # # ChatGpt("Who is the wife of Salman Khan")
# # # ChatGpt("integration of tanx")
# # # ChatGpt("Describe life")
# # # ChatGpt("What is psycopg2")


import os
from g4f.client import Client
import time

def ChatGpt(*messages):
    client = Client()

    def retry_request(func, max_retries=3, delay=1):
        retries = 0
        while retries < max_retries:
            try:
                return func()
            except Exception as e:
                print(f"Error: {e}. Retrying...")
                retries += 1
                time.sleep(delay * (2 ** retries))
        raise Exception("Max retries exceeded. Unable to complete the request.")

    try:
        response = retry_request(lambda: client.chat.completions.create(
            model="gpt-4-32k-0613",
            messages=[{"role": "user", "content": msg} for msg in messages],
            stream=True,
        ))

        response_str = ""
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                response_str += chunk.choices[0].delta.content

        if not response_str:
            print("Empty response received from the API.")

        print(response_str.encode('utf-8', 'ignore').decode('utf-8'), end="", flush=True)
        print()

        return response_str

    except Exception as e:
        print("An error occurred:", str(e))
        return ""

# Example usage
ChatGpt("Give a hello world code in c")

