import os
import speech_recognition as sr 
import webbrowser
import pyttsx3
import time
import pyaudio
import music_library
from newsapi import NewsApiClient
import wikipedia


recognizer = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose a smooth voice by index
engine.setProperty('rate', 150)            # Lower rate for smoother speech
engine.setProperty('volume', 0.9)          # Optional: adjust volume



def speak(text):
    engine.say(text)
    engine.runAndWait()

def ProcessCommand(c):

    if "headlines" in c.lower() or "headline" in c.lower():
        # Initialize with your API key
        newsapi = NewsApiClient(api_key="") #use your own api key

        # Fetch top headlines globally
        top_headlines = newsapi.get_top_headlines(language='en')
        news_titles = [article['title'] for article in top_headlines['articles'][:5]]  # top 5 headlines
        text_to_speak = "Here are the top headlines: " + ". ".join(news_titles)
        engine.say(text_to_speak)
        engine.runAndWait()

    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com")
    elif "play " in c.lower():
        song = c[5:].strip().lower()  # convert input to lowercase and takes all the words after play
        link = music_library.music.get(song)  # look up using lowercase key
        if link:
            webbrowser.open(link)
        else:
            print(f"Song '{song}' not found in music library.")

    elif "wikipedia" in c.lower():
        try:
            query=c.lower().replace("wikipedia","").strip() #Removes the word "wikipedia" from the command to isolate what the user wants to search Converts the command to lowercase to normalize it.
                                                           
            for phrase in ["who is", "what is", "tell me about", "search", "can you tell me about"]:# Remove question phrases (add more as needed)
                if query.startswith(phrase):
                    query = query.replace(phrase, "").strip()
        
            if query=="":                                  
                speak("what do you want to search on wikipedia")  #if the user did not speak anything we ask them to speak
                return
            print("searching for", query)
            summary = wikipedia.summary(query,sentences=2) #Fetches a summary from Wikipedia for the given query limits to 2 sentences
            speak("according to wikipedia" + summary)
        except wikipedia.exceptions.DisambiguationError:
            speak("The topic is too ambiguous. Please specify.")
        except wikipedia.exceptions.PageError:
            speak("No Wikipedia page found for your query.")
        except Exception as e:
            speak("An error occurred while searching Wikipedia.")     



if __name__ == "__main__":
    speak("Initializing jarvis..")
    #listen for the wake word jarvis
    # obtain audio from the microphone
    r = sr.Recognizer()


    print("recognizing...")
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(word)

            if(word.lower()== "jarvis"):
                engine.say("yes")
                #listen for command        
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    ProcessCommand(command)
               
                
            
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print("Error; {0}".format(e))

            time.sleep(1)
