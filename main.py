import threading
import sys
import AI.Ai as Ai
import Speech
from MessageOSC.SendOSC import SendMessageBox
from Speech.SpeecRec.SpeechRec import recognize_speech

def start_recognition_thread():
    # Create a new thread for running speech recognition continuously
    speech_thread = threading.Thread(target=recognize_speech, args=(process_text,))
    
    # Start the thread
    speech_thread.start()
    speech_thread.join()

def process_text(text):
    print("Received text:", text)
    if (text != ""): 
        response = Ai.SpeekToAI(text)
        SendMessageBox(response)
        Speech.say(response)
    # Perform further actions or call other functions based on the recognized text

# Call this function to start the speech recognition thread whenever needed
start_recognition_thread()