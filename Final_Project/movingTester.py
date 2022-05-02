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

    # Motor 5: Whole arm up and down (shoulder)
    # Motor 6: Whole arm in and out (between shoulder and elbow)
        # be careful, values over 6000 move arm into robot and hits it
    # Motor 7: Elbow bend and straighten
    # Motor 8: Wrist bend and straighten - 8000 seems to be max close
    # Motor 9: Hand rotate
    # Motor 10: Hand close and open

    def armReady(self):   #Straightens arm, is about 30 degrees from straight down
        self.methods.positionMotor(6, 6000)
        #sleep(1)
        self.methods.positionMotor(7, 4000)
        #sleep(1)
        self.methods.positionMotor(8, 6000)
        #sleep(1)
        self.methods.positionMotor(9, 6000)
        #sleep(1)
        self.methods.positionMotor(10, 8000)
        
        sleep(1)

        #motors 6 and 7 i think are moving 5 so theres not much point using it unless its the last one changed
        #self.methods.positionMotor(5, 6000)
        #sleep(1)


    def armDefaultAttack(self):
        self.methods.positionMotor(5, 10000)
        sleep(.5)
        self.sound.CreateSound("spell.mp3", 'Expelliarmus')
        self.sound.PlaySound("spell.mp3")
        self.methods.positionMotor(7, 6000)
        self.methods.positionMotor(5, 8000)
        sleep(1)
        self.armReady()
        

    def armCritAttack(self):
        self.methods.positionMotor(2, 4000)
        self.methods.positionMotor(5, 10000)
        sleep(.5)
        self.sound.CreateSound("spell.mp3", 'Avada Kedavra')
        self.sound.PlaySound("spell.mp3")
        self.methods.positionMotor(2, 6000)
        self.methods.positionMotor(7, 6000)
        self.methods.positionMotor(5, 8000)
        sleep(1)
        self.armReady()
        

    def armMissAttack(self):
        self.methods.positionMotor(2, 4000)
        self.methods.positionMotor(5, 10000)
        sleep(.5)
        self.sound.CreateSound("spell.mp3", 'Lumos')
        self.sound.PlaySound("spell.mp3")
        self.methods.positionMotor(7, 6000)
        self.methods.positionMotor(5, 8000)
        sleep(1)
        self.methods.positionMotor(2, 6000)
        sleep(1)
        self.armReady()

    def takeDamage(self):
        #shake head
        self.methods.positionMotor(3, 8000)
        sleep(.1)
        self.methods.positionMotor(3, 4000)
        sleep(.1)
        # self.methods.positionMotor(3, 8000)
        # sleep(.1)
        # self.methods.positionMotor(3, 4000)
        # sleep(.1)
        # self.methods.positionMotor(3, 8000)
        # sleep(.1)
        # self.methods.positionMotor(3, 4000)
        # sleep(.1)
        self.methods.positionMotor(3, 6000)
        sleep(.1)
        #turn and cover
        self.methods.positionMotor(2, 8000)
        sleep(.1)
        self.methods.positionMotor(5, 10000)
        sleep(2)
        self.methods.positionMotor(2, 6000)
        sleep(1)
        self.armReady()

    def rechargeMove(self):
        self.methods.positionMotor(4, 8000)
        sleep(.1)
        self.methods.positionMotor(6, 4000)
        sleep(.1)
        self.methods.positionMotor(5, 10000)
        sleep(3)
        self.methods.positionMotor(4, 6000)
        sleep(.1)
        self.methods.positionMotor(6, 6000)
        sleep(1)
        self.armReady()
        
    def boostMove(self):
        self.methods.positionMotor(4, 4500)
        sleep(.1)
        self.methods.positionMotor(3, 4500)
        sleep(.1)
        self.methods.positionMotor(5, 7000)
        sleep(1)
        self.methods.positionMotor(4, 7500)
        sleep(.1)
        self.methods.positionMotor(7, 6000)
        self.methods.positionMotor(5, 10000)
        sleep(3)
        self.methods.positionMotor(4, 6000)
        sleep(.1)
        self.methods.positionMotor(3, 6000)
        sleep(.1)
        self.armReady()


