import time
import speech_recognition as sr

class Methods:
    usb = None

    def __init__(self, usb):
        self.usb = usb

    #what is actually running the command
    def positionMotor(self, motorNum, position, duration):
        if motorNum != 100:
            lsb = position &0x7F
            msb = (position >> 7) & 0x7F
            motor = chr(0x0 + motorNum)
            cmd = chr(0xaa) + chr(0xC) + chr(0x04) + motor + chr(lsb) + chr(msb)
            self.usb.write(cmd.encode('utf-8'))
        
        if duration != 0:
            time.sleep(duration)
        else:
            time.sleep(0.25)

    def speak(outputString):
        print(outputString)

    def waitForCommand(inputSpring):
        speech = True
        while speech:
            with sr.Microphone() as source:
                r= sr.Recognizer()
                r.adjust_for_ambient_noise(source)
                r.dyanmic_energythreshhold = 3000
                
                try:
                    print("listening")
                    audio = r.listen(source)            
                    print("Got audio")
                    word = r.recognize_google(audio)
                    print(word)
                    if inputSpring in word:
                        speech = False
                except sr.UnknownValueError:
                    print("Don't knoe that werd")