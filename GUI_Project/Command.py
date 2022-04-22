from Methods import *
#import serial
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
        if len(self.exeType) == len(' Robot move for') and self.exeType == 'move forward':
            if(self.exeDuration > 0):
                print("TYPE: move forward")
                self.methods.positionMotor(0, 6000, 0)
                self.methods.positionMotor(0, 4500, self.exeDuration)
                self.methods.positionMotor(0, 6000, 0)
            else:
                print("TYPE: move backward")
                self.methods.positionMotor(0, 6000, 0)
                self.methods.positionMotor(0, 7500, abs(self.exeDuration))
                self.methods.positionMotor(0, 6000, 0)

        elif len(self.exeType) == len('turn right') and self.exeType == 'turn right':
            print("TYPE: turn right")
            self.methods.positionMotor(0, 6000, 0)
            self.methods.positionMotor(1, 4900, 0)

        elif len(self.exeType) == len('turn left') and self.exeType == 'turn left':
            print("TYPE: turn left")
            self.methods.positionMotor(0, 6000, 0)
            self.methods.positionMotor(1, 7150, 0)

        elif len(self.exeType) == len('head tilt') and self.exeType == 'head tilt':
            print("TYPE: head tilt")
            self.methods.positionMotor(4, 6000 + self.exeAngle, 0)

        elif len(self.exeType) == len('head pan') and self.exeType == 'head pan':
            print("TYPE: head pan")
            self.methods.positionMotor(3, 6000 - self.exeAngle, 0)

        elif len(self.exeType) == len('waist') and self.exeType == 'waist':
            print("TYPE: waist")
            self.methods.positionMotor(2, 6000 - self.exeAngle, 0)

        elif len(self.exeType) == len('pause') and self.exeType == 'pause':
            print("TYPE: pause")
            self.methods.positionMotor(100, 0, self.exeDuration)

        elif len(self.exeType) == len('speak') and self.exeType == 'speak':
            print('TYPE: speak')
            self.methods.speak(self.exeAngle)

        elif len(self.exeType) == len('wait for') and self.exeType == 'wait for':
            print('TYPE: wait for ' + self.exeAngle)
            self.methods.waitForCommand(self.exeAngle)
