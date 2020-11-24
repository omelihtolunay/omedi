import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import Tokenizer
from gtts import gTTS
from time import ctime
r= sr.Recognizer()


def record_audio(ask = False):
	with sr.Microphone() as source:

		if ask:
			jamal_speak(ask)

		print('Say something.. ')
		audio = r.listen(source)
		voice_data = ''
		try:		
			voice_data = r.recognize_google(audio,language="en")
			jamal_speak(voice_data)

		except sr.UnknownValueError:
			jamal_speak('Please repeat, could not understand')

		except sr.RequestError:
			jamal_speak("Could not understand..")

		return voice_data 

def omedi_speak(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r =  random.randint(1,10000000)
	audio_file = 'audio-'+str(r)+'.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)


def respond(voice_data):
	if "what is your name" in voice_data:
		jamal_speak('My name is OMEDI')

	if "what time is it " in voice_data:
		jamal_speak(ctime())

	if "search" in voice_data:
		search = record_audio('NWhat do you want to search for...')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		jamal_speak('Search result: ')


	if "where" in voice_data:
		location = record_audio('Where do you want to find.')
		url = 'https://google.nl/maps/place+' + location +'/&amp;'
		webbrowser.get().open(url)
		jamal_speak('location that you search: ')

	if "exit" in voice_data:
		exit()

time.sleep(1)


omedi_speak('How can I help you?')

while 1:
	voice_data= record_audio()
	respond(voice_data)