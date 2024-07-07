import os
import sys
import pygame
import requests
import webbrowser
import musicLibrary
from os import system
from gtts import gTTS
import speech_recognition as sr
import google.generativeai as genai


recognizer=sr.Recognizer()
newsapi = "NEWS_KEY"

# Configure Google Generative AI
genai.configure(api_key="KEY")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2049
}
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

# Initialize Pygame mixer
pygame.mixer.init()

def speaker_OLD(text):
    system("say {}".format(text))

def speaker(text,speed=1.25):
    
    text=text.lower()
    tts = gTTS(text)
    
    tts.save('temp.mp3') 

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # # Keep the program running until the music stops playing
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(10)

    max_time = 10  # Maximum duration in seconds
    start_time = pygame.time.get_ticks() / 1000  # Start time in seconds

    while pygame.mixer.music.get_busy():
        # Check if maximum time exceeded
        current_time = pygame.time.get_ticks() / 1000  # Current time in seconds
        if current_time - start_time > max_time:
            break
        
        pygame.time.Clock().tick(10)  # Adjust the tick rate to control playback
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    try:
        response = model.generate_content([command])
        return response.text
    except Exception as e:
        print(f"Error generating content: {e}")
        return "I'm sorry, I couldn't process your request."
    
def processCommand(c):
    # if "open google" in c.lower():
    #     webbrowser.open("https://google.com")
    #     speaker("opening google")
    # elif "open facebook" in c.lower():
    #     webbrowser.open("https://facebook.com")
    #     speaker("opening facebook")
    # elif "open youtube" in c.lower():
    #     webbrowser.open("https://youtube.com")
    #     speaker("opening youtube")
    # elif "open linkedin" in c.lower():
    #     webbrowser.open("https://linkedin.com")
    #     speaker("opening linkedin") 
    if "open" in c.lower():
        command=c.lower().split(" ")[1]
        webbrowser.open(f"https://{command}.com")
        speaker(f"opening {command}")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speaker(f"playing {song}")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            speaker("todays news")
            for article in articles:
                speaker(article['title'])

    else:
        # Let AI handle the request
        speaker("lets ask a i")
        output = aiProcess(c)
        speaker(output) 

if __name__=="__main__":
    speaker("Initializing friday....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                print("recognizing...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(f"you said {word}")
            if("hey" in word.lower() or "friday" in word.lower()):
                speaker("hii taarak")
                # Listen for command
                with sr.Microphone() as source:
                    print("Friday Active...")
                    speaker("ask me anything")
                    # audio = r.listen(source)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    print(command)
                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

