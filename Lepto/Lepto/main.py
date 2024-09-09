import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="28acdd2c839e4da0a958988f0cda9d56"

def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen for a stop command
def listen_for_stop():
    stop_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 'stop' command...")
        audio = stop_recognizer.listen(source, timeout=2, phrase_time_limit=2)
        try:
            command = stop_recognizer.recognize_google(audio)
            if "stop" in command.lower():
                return True
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return False




def processCommand(c):
    if "open google"in c.lower():
       webbrowser.open("https://google.com")
    elif "open youtube"in c.lower():
       webbrowser.open("https://youtube.com")
    elif "open instagram"in c.lower():
       webbrowser.open("https://instagram.com")

    elif "open linkdin"in c.lower():
        webbrowser.open("https://linkdin.com")
    elif "open triple i t kota"in c.lower():
        webbrowser.open("https://iiitkota.ac.in")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ",1)[1]
        link=music.music[song]
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in the music librabry.")
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # Limit to first 5 headlines
                speak(article['title'])
        else: 
            speak("Failed to retrieve news.")
    else:
        #let open ai handle the request
        pass
        


if __name__=="__main__":
    speak("Initializing Lepto....")
    while True:
        #listen for the wake word lepto
        #obtain audio from the microphoen
        r=sr.Recognizer()
        
        speak("Recognizing...")
            #recognise speech using sphinx
        try:
           with sr.Microphone() as source:
                print("Listing...")
                audio=r.listen(source,timeout=2,phrase_time_limit=5)
           word=r.recognize_google(audio)

           if(word.lower()=="laptop"):
               speak("Yes sir?")
               #listen for command 
               print("Awaiting command...")
               with sr.Microphone() as source:
                    print("Activating Lepto...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)

       
        except Exception as e:
            print("Lepto error;{0}".format(e))
