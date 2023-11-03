import gtts
import os
import pygame
import pygame.mixer
import time

def play_mp3(file_path):
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Set the output device (optional)

    pygame.mixer.pre_init(devicename="CABLE Input (VB-Audio Virtual Cable)")
    # Load the MP3 file
    pygame.mixer.music.load(file_path)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up resources
    pygame.mixer.quit()


def say(text):
    tts = gtts.gTTS(text)
    os.remove('output.mp3')
    tts.save('output.mp3')
    play_mp3("output.mp3")

