from Methods import *
import serial
class Command:
    exeDuration = 0
    exeType = ''
    exeAngle = 0
    methods = ''
    
    def __init__(self, inTime, inType, inAngle):
        # Duration the movement will be executed
        self.exeTime = inTime
        
        # Type of motion that will be executed
        self.exeType = inType
        
        # Angle for rotation or movement or string
        self.exeAngle = inAngle
        usb = serial.Serial('/dev/ttyACM0')
        print (usb.name)
        print(usb.baudrate)
        self.methods = Methods(usb)


    def ExecuteCommand(self):
        # exeType can be integers or strings or any type of variable
        # whatever works best.
        print(self.exeType)
        if len(self.exeType) == len('move forward') and self.exeType == 'move forward':
            print("TYPE: move forward")
            self.methods.positionMotor(0, 6000, 0)
            self.methods.positionMotor(0, 4500, self.exeDuration)
            self.methods.positionMotor(0, 6000, 0)
        elif len(self.exeType) == len('move backward') and self.exeType == 'move backward':
            print("TYPE: move back")
            self.methods.positionMotor(0, 6000, 0)
            self.methods.positionMotor(0, 7500, self.exeDuration)
            self.methods.positionMotor(0, 6000, 0)
        elif len(self.exeType) == len('turn right') and self.exeType == 'turn right':
            print("TYPE: turn right")
            self.methods.positionMotor(0, 6000, 0)
            self.methods.positionMotor(1, 4900, 0)
        elif len(self.exeType) == len('turn left') and self.exeType == 'turn left':
            print("TYPE: turn left")
            self.methods.positionMotor(0, 6000, 0)
            self.methods.positionMotor(1, 7150, 0)
        elif len(self.exeType) == len('head up') and self.exeType == 'head up':
            print("TYPE: head up")
            self.methods.positionMotor(4, self.exeAngle, 0)
        elif len(self.exeType) == len('head down') and self.exeType == 'head down':
            print("TYPE: head down")
            self.methods.positionMotor(4, self.exeAngle, 0)
        elif len(self.exeType) == len('head left') and self.exeType == 'head left':
            print("TYPE: head left")
            self.methods.positionMotor(3, self.exeAngle, 0)
        elif len(self.exeType) == len('head right') and self.exeType == 'head right':
            print("TYPE: head right")
            self.methods.positionMotor(3, self.exeAngle, 0)
        elif len(self.exeType) == len('waist right') and self.exeType == 'waist right':
            print("TYPE: waist right")
            self.methods.positionMotor(2, self.exeAngle, 0)
        elif len(self.exeType) == len('waist left') and self.exeType == 'waist left':
            print("TYPE: waist left")
            self.methods.positionMotor(2, self.exeAngle, 0)
        elif len(self.exeType) == len('pause') and self.exeType == 'pause':
            print("TYPE: pause")
            self.methods.positionMotor(100, 0, self.exeDuration)
        elif len(self.exeType) == len('speak') and self.exeType == 'speak':
            print('TYPE: speak')
            self.methods.speak(self.exeAngle)
        elif len(self.exeType) == len('wait for') and self.exeType == 'wait for':
            print('TYPE: wait for ' + self.exeAngle)
            self.methods.waitForCommand(self.exeAngle)
