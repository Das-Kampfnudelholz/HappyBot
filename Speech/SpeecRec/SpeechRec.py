import speech_recognition as sr
from MessageOSC.SendOSC import SendMessageBox
def recognize_speech(callback_func):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        
        while True:  
            audio = r.listen(source, phrase_time_limit=1)  
            
            try:
                text = r.recognize_whisper(audio)
                if text.lower().startswith("hey happy"):
                    SendMessageBox("I'm listening")
                    audio = r.listen(source, phrase_time_limit=1) 
                    text = r.recognize_whisper(audio)
                    callback_func(text.lower())      
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error: {str(e)}")