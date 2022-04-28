from time import sleep
from Methods2 import *
import serial

class MoveTester:

    def __init__(self):
        
        usb = serial.Serial('/dev/ttyACM0')
        self.methods = Methods(usb)

    def MoveToNextNode(self):
        self.methods.positionMotor(0, 6000)
        sleep(.25)
        self.methods.positionMotor(0, 5000)
        sleep(.6)
        self.methods.positionMotor(0, 6000)
        sleep(.25)

    def TurnLeft(self):
        turnPosition = 6000
        self.methods.positionMotor(0, 6000)
        #self.methods.positionMotor(1, 6000)
        sleep(.25)
        print("left")
        self.methods.positionMotor(1, 7200)
        sleep(.25)
        print("left 1")
        self.methods.positionMotor(0, 6000)
        self.methods.positionMotor(1, 7200)
        sleep(.25)
        print("left 2")
        self.methods.positionMotor(0, 6000)
        self.methods.positionMotor(1, 7200)
        sleep(.25)
        print("left 3")
        self.methods.positionMotor(0, 6000)
        self.methods.positionMotor(1, 7200)
        sleep(.25)
        print("left 4")


    def TurnRight(self):
        turnPosition = 6000
        self.methods.positionMotor(0, 6000)
        #self.methods.positionMotor(1, 6000)
        sleep(.25)
        print("right")
        self.methods.positionMotor(1, 4900)
        sleep(.25)
        print("right 1")
        self.methods.positionMotor(0, 6000)
        self.methods.positionMotor(1, 4900)
        sleep(.25)
        print("right 2")
        self.methods.positionMotor(0, 6000)
        self.methods.positionMotor(1, 4900)
        sleep(.25)
        print("right 3")
        self.methods.positionMotor(0, 6000)
        self.methods.positionMotor(1, 4900)
        sleep(.25)
        print("right 4")

    def ArmDefault(self):   #Straightens arm, is about 30degrees off 
        self.methods.positionMotor(5, 6000)
        sleep(1)
        self.methods.positionMotor(6, 6000)
        sleep(1)
        self.methods.positionMotor(7, 6000)
        sleep(1)
        self.methods.positionMotor(8, 6000)
        sleep(1)
        self.methods.positionMotor(9, 6000)
        sleep(1)
        self.methods.positionMotor(10, 6000)
        sleep(1)

    def ArmMove(self):
        # Motor 5: Whole arm up and down (shoulder)
        # Motor 6: Whole arm in and out (between shoulder and elbow)
            # be careful, values over 6000 move arm into robot and hits it
        # Motor 7: Elbow bend and straighten
        # Motor 8: Wrist bend and straighten
        # Motor 9: Hand rotate
        # Motor 10: Hand close and open

        self.methods.positionMotor(5, 7000)
        sleep(1)
        self.methods.positionMotor(6, 7000)
        sleep(1)
        self.methods.positionMotor(7, 7000)
        sleep(1)
        self.methods.positionMotor(8, 7000)
        sleep(1)
        self.methods.positionMotor(9, 7000)
        sleep(1)
        self.methods.positionMotor(10, 7000)
        sleep(1)

    def secondArm(self):
        # self.methods.positionMotor(5, 8000)
        # sleep(1.5)
        self.methods.positionMotor(6, 4000)
        sleep(1)
        self.methods.positionMotor(5, 8000)
        # self.methods.positionMotor(6, 6000)
        # sleep(1)
        # self.methods.positionMotor(5, 6000)
        # sleep(1)
        

test = MoveTester()
# test.MoveToNextNode()
# test.TurnLeft()
# test.MoveToNextNode()
# test.TurnRight()
# test.MoveToNextNode()
# test.TurnLeft()
# test.TurnLeft()
# test.MoveToNextNode()
# test.TurnLeft()
# test.TurnRight()
test.secondArm()
