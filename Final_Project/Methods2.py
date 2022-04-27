import time, sys
#from Robot import *

class Methods:
    usb = None
    #robot = ROBOT()

    def __init__(self, usb):
        self.usb = usb

    def testThis():
        #print(num)
        print("here")

    #what is actually running the command
    def positionMotor(self, motorNum, position):
        lsb = position &0x7F
        msb = (position >> 7) & 0x7F
        motor = chr(0x0 + motorNum)
        cmd = chr(0xaa) + chr(0xC) + chr(0x04) + motor + chr(lsb) + chr(msb)
        self.usb.write(cmd.encode('utf-8'))
        time.sleep(0.25)

    #move head left
    def headMoveLeft(self, event):
        if(self.robot.headLR < 8000):
            self.robot.headLR += 500
            self.positionMotor(3, self.robot.headLR)
            print('Move head left')
    #move head right
    def headMoveRight(self, event):
        if(self.robot.headLR > 4000):
            self.robot.headLR -= 500
            self.positionMotor(3, self.robot.headLR)
            print('Move head right')

    #move head down
    def headMoveDown(self, event):
        if(self.robot.headUD > 4000):
            self.robot.headUD -= 500
            self.positionMotor(4, self.robot.headUD)
            print('Move head down')
    #move head up
    def headMoveUp(self, event):
        if(self.robot.headUD < 8000):
            self.robot.headUD += 500
            self.positionMotor(4, self.robot.headUD)
            print('Move head up')

    #move waist left
    def waistMoveLeft(self, event):
        if(self.robot.waist < 8000):
            self.robot.waist += 500
            self.positionMotor(2, self.robot.waist)
            print('Rotate waist left')

    #move waist right
    def waistMoveRight(self, event):
        if(self.robot.waist > 4000):
            self.robot.waist -= 500
            self.positionMotor(2, self.robot.waist)
            print('Rotate waist right')
            
    #turn robot left
    def robotMoveLeft(self, event):
        self.positionMotor(0, 6000)
        self.robot.driveRL = 7150
        self.positionMotor(1, self.robot.driveRL)
        print('Move left')
        self.robot.driveFB = 6000
    
    #move robot forward
    def robotMoveForward(self, event):
        if(self.robot.driveFB > 3750):
            self.positionMotor(0, 6000)
            self.robot.driveFB -= 750
            self.positionMotor(0, self.robot.driveFB)
            print('Move forward')
            
    #turn robot right
    def robotMoveRight(self, event):
        self.positionMotor(0, 6000)
        self.robot.driveRL = 4900
        self.positionMotor(1, self.robot.driveRL)
        print('Move right')
        self.robot.driveFB = 6000

    #move robot backwards
    def robotMoveBackwards(self, event):
        if(self.robot.driveFB < 8250):
            self.positionMotor(0, 6000)
            self.robot.driveFB += 750
            self.positionMotor(0, self.robot.driveFB)
            print('Move backward')
            
    #breaks out of program        
    def endLife(self, event):
        print('DIE')
        sys.exit(0)
            
    #centers body motors to position 6000
    def center(self, event):
        self.robot.driveFB = 6000
        self.robot.waist = 6000
        self.robot.headLR = 6000
        self.robot.headUD = 6000
        for item in range(2, 5):
            self.positionMotor(item, 6000)
        print('Centering in the methods')
