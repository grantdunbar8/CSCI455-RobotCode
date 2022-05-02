import speech_recognition as speech
import time

# 7 seconds
#life = time.time() + 7

class Mic:
    # def __init__(self):
    #     self.life = life
    
    def Listen(self):
        life = time.time() + 7
        print("Begin collection of mic data for " + str(life) + " seconds.")
        print("The time: " + str(time.time()) + " Life: " + str(life))
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
                    return data
                    # Do something with data here
                    # return data?
                except speech.UnknownValueError:
                    print("ERROR: Unknown data at Mic class.")
