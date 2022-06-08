# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:14:52 2022

@author: MEHER
"""


import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.get_default_graph()
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import random
import os
import smtplib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
app = Flask(__name__)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wish',methods = ['GET','POST'])
def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning!")
        
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<23:
        speak("Good Evening!")

    else:
        speak("Its late sir, but I am here.")
        
    speak("my name is Alpha. Please tell me how can I help you madam")
    while True:
        query = takeCommand().lower()
        print(query)
        if 'stop listening' or 'stop' in query:
            c = random.randrange(0,2,1)
            if c==0: 
                speak("I will wait for your command")
            elif c==1:
                speak("Ok sir")
                break
        stop_words=set(stopwords.words('english'))
        word_tokens=query.split(" ")
        q=[]
        for w in word_tokens:
            if w not in stop_words and w.lower()!="this" and w.lower()!="that" and w.lower()!="the" and w.lower()!="your" and w.lower()!="what":
                q.append(w)
        file=open(r"C:\Users\MEHER\Documents\Base.txt") 
        content=[]
        k=file.readlines()
        for i in k:
            content.append(i)
        f=0
        print(q)
        #print(q,word_tokens)
        #print(content[0])
        for i in word_tokens:
            for j in content:
                if i.lower() in j.lower():
                    print(j)
                    speak(j)
                    f=1
                    break
            if f==1:        
                break

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #its takes mic input and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        speak("Sorry, I could not get that")
        speak("Say that again please...")
        return "None"
    
    return query    
#wishMe()
            
            




if __name__ == '__main__':
    app.run(debug = False, threaded = False)