import speech_recognition as speech
import time

# 7 seconds
life = time.time() + 7

class Mic:
    def __init__():
    
    def Listen(self):
        print("Begin collection of mic data for " + life + " seconds.")
        while time.time() <= life:
            if time.time() > life:
                break
            
            with speech.Microphone() as source:
                recognizer = speech.Recognizer()
                recognizer.adjust_for_ambient_noise(source)
                recognizer.dyanmic_energythreshhold = 3000
                
                try:
                    print("MIC: Listening.")
                    audio = recognizer.listen(source)            
                    print("MIC: Got audio.")
                    data = recognizer.recognize_google(audio)
                    print(data)
                    # Do something with data here
                    # retrun data
                except speech.UnknownValueError:
                    print("ERROR: Unknown data at Mic class.")
