'''
__/\\\\\\\\\\\\\_______/\\\\\\\\\_____/\\\________/\\\__/\\\____________________________/\\\________/\\\_____/\\\\\\\_______/\\\\\\\\\_____        
 _\/\\\/////////\\\___/\\\\\\\\\\\\\__\/\\\_______\/\\\_\/\\\___________________________\/\\\_______\/\\\___/\\\/////\\\___/\\\///////\\\___       
  _\/\\\_______\/\\\__/\\\/////////\\\_\/\\\_______\/\\\_\/\\\___________________________\//\\\______/\\\___/\\\____\//\\\_\///______\//\\\__      
   _\/\\\\\\\\\\\\\/__\/\\\_______\/\\\_\/\\\_______\/\\\_\/\\\______________/\\\\\\\\\\\__\//\\\____/\\\___\/\\\_____\/\\\___________/\\\/___     
    _\/\\\/////////____\/\\\\\\\\\\\\\\\_\/\\\_______\/\\\_\/\\\_____________\///////////____\//\\\__/\\\____\/\\\_____\/\\\________/\\\//_____    
     _\/\\\_____________\/\\\/////////\\\_\/\\\_______\/\\\_\/\\\______________________________\//\\\/\\\_____\/\\\_____\/\\\_____/\\\//________   
      _\/\\\_____________\/\\\_______\/\\\_\//\\\______/\\\__\/\\\_______________________________\//\\\\\______\//\\\____/\\\____/\\\/___________  
       _\/\\\_____________\/\\\_______\/\\\__\///\\\\\\\\\/___\/\\\\\\\\\\\\\\\____________________\//\\\________\///\\\\\\\/____/\\\\\\\\\\\\\\\_ 
        _\///______________\///________\///_____\/////////_____\///////////////______________________\///___________\///////_____\///////////////__
  ___        _____                         _   _ _                   ___   ___ ___   _____ __ ___ ___ 
 | _ )_  _  |_   _|_ _ _ _  _ _  ___ _ _  | | | | |_ ___  ___ _ _   ( _ ) / / ( _ ) / /_  )  \_  )_  )
 | _ \ || |   | |/ _` | ' \| ' \/ -_) '_| | |_| |  _|_ / / _ \ ' \  / _ \/ /| / _ \/ / / / () / / / / 
 |___/\_, |   |_|\__,_|_||_|_||_\___|_|    \___/ \__/__| \___/_||_| \___/_/ |_\___/_/ /___\__/___/___|
      |__/                   
'''
from cProfile import run
from pocketsphinx import LiveSpeech
import pyttsx3
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
from paulsListening import Recorder
from paulsAnalysis import Analysis
import paulsMemory
import time

# Setup Speach Recognition
audioRecognizer = sr.Recognizer()
freq = 16000
duration = 5
tempSpeechFile = 'C:\\Users\\master\\Documents\\PAUL\\temp\\tempRecording.wav'

# Setup Live Speech for Keyword
activeSpeech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    lm=False, 
    keyphrase='paul', # only use one word phrase search, multi words adds failure and complexity
    kws_threshold=1e-11 #Goes from 1e-1 to 1e-50
)

# Setup Text to Speech
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id) # Lol 9 is indian, 3 is the guy that sounds normal

# Additional things to setup
paulsMemory.initialize()
recordLoud = Recorder()
analyseText = Analysis()

# Key Notes: Sometimes keyphrase can get called multiple time by accident (This is my only issue that makes this run like shit)
for phrase in activeSpeech:

    time.sleep(0.5)
    engine.say('Yea')
    engine.runAndWait()

    # Pull Audio files from class
    recordLoud.listen()

    # Write and decode the needed audio files
    tempAudioRec = sr.AudioFile('C:\\Users\\master\\Documents\\PAUL\\temp\\tempRec.wav')
    with tempAudioRec as source:
        audio = audioRecognizer.record(source)
    type(audio)

    engine.say('gocha')
    engine.runAndWait()

    # Define user speech and relay results to the consol - We have a try/except in the case nothing can be understood by recognize_sphinx()
    try:
        sysHeard = audioRecognizer.recognize_sphinx(audio)
        print('User speech has been recognized as: ', sysHeard)

        # Here is where paulsDecision will be called and this will be used to keep this script light so we can make the sr better
        # --- Well need to send current time to the decision class from this instance
        engine.say((analyseText.makeDecision(sysHeard)))
        engine.runAndWait()

    except:
        pass
        print("System error handled. User didn't say anything")