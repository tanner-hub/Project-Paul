import pyttsx3
import pygame
import time
from pocketsphinx import LiveSpeech
import os

def main():
    pygame.mixer.init()

    pygame.mixer.music.load('./mp3/ShortPaul.mp3')
    pygame.mixer.music.play()
    time.sleep(3)

    print('Running Paul Live Speech...')

    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        lm=False, 
        keyphrase='play',
        kws_threshold=1e-20
    )

    for phrase in speech:
        pygame.mixer.music.load('./mp3/floaton.mp3')
        pygame.mixer.music.play()
        time.sleep(220)

if __name__ == "__main__":
    while True: main()