from tkinter import *
from ast import excepthandler
from unittest import case
import serial, os
from Methods import *
import speech_recognition as sr
import _thread, threading

# initialize usb connection
try:
    usb = serial.Serial('/dev/ttyACM0')
    print (usb.name)
    print(usb.baudrate)
    
except:
    try:
        usb = serial.Serial('/dev/ttyACM1')
        print (usb.name)
        print (usb.baudrate)
    except:
        print("No servo serial ports found")

# enables window for Tk
if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')


class ThreadExample:
    def __init__(self):
        self.count = 100
        self.message = 0

    def firstThread(self, root, methods):
        speech = TRUE
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

                    if 'head left' in word or 'had left' in word:
                        methods.headMoveLeft(word)
                    if 'head right' in word or 'had right' in word:
                        methods.headMoveRight(word)
                    if 'head down' in word or 'had down' in word:
                        methods.headMoveDown(word)
                    if 'head up' in word or 'had up' in word:
                        methods.headMoveUp(word)

                    if 'body left' in word or 'waist left' in word or 'waste left' in word:
                        methods.waistMoveLeft(word)
                    if 'body right' in word or 'waist right' in word or 'waste right' in word:
                        methods.waistMoveRight(word)

                    if 'turn left' in word or 'spin left' in word:
                        methods.robotMoveLeft(word)
                    if 'turn right' in word or 'spin right' in word:
                        methods.robotMoveRight(word)
                    if 'forward' in word or 'speed up' in word:
                        methods.robotMoveForward(word)
                    if 'backward' in word or 'slow down' in word:
                        methods.robotMoveBackward(word)

                    if 'stop' in word or 'Stop' in word:
                        methods.stop(word)
                    if 'center' in word or 'Center' in word:
                        methods.center(word)
                    if 'brake' in word or 'break' in word or 'die' in word:
                        methods.endLife(word)
                
                except sr.UnknownValueError:
                    print("Don't knoe that werd")
        



    
    def secondThread(self, root, methods):
        root.bind('<a>', methods.headMoveLeft)
        root.bind('<d>', methods.headMoveRight)
        root.bind('<w>', methods.headMoveDown)
        root.bind('<s>', methods.headMoveUp)
        root.bind('<Up>', methods.robotMoveForward)
        root.bind('<Left>', methods.robotMoveLeft)
        root.bind('<Right>', methods.robotMoveRight)
        root.bind('<Down>', methods.robotMoveBackwards)
        root.bind('<b>', methods.endLife)
        root.bind('<z>', methods.waistMoveLeft)
        root.bind('<x>', methods.waistMoveRight)
        root.bind('<c>', methods.center)
        root.bind('<h>', methods.stop)
        

inst = ThreadExample()
root = Tk()
methods = Methods(usb)


try:
    _thread.start_new_thread(inst.firstThread,(root, methods))
    _thread.start_new_thread(inst.secondThread,(root, methods))
except:
    print("ERROR - thread no started")

root.mainloop()






# sets keybinds

