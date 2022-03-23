from tkinter import *
from ast import excepthandler
import serial, os
from Methods import *

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

# sets keybinds
root = Tk()
methods = Methods(usb)
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
root.mainloop()
