import time, sys
from Robot import *

class Methods:
    usb = None
    robot = ROBOT()

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
        print('waiting for ' + inputSpring)