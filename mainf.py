import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
r=sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak("Sorry,my speech service is down")
        return voice_data
def speak(audio_str):
    tts=gTTS(text=audio_str,lang='en')
    r=random.randint(1,1000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_str)
    os.remove(audio_file)

def respond(voice_data):
    if "hi" in voice_data:
        speak('Hi! How can I help you')
    if "what is the time" in voice_data:
        speak(ctime())
    if "search" in voice_data:
        search=record_audio('What do you want to search for?')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak('here is what I found for '+search)
    if 'thank you' in voice_data:
        exit()
#time.sleep(1)
speak('How can I help you....')
while 1:
    voice_data=record_audio()
    respond(voice_data)
