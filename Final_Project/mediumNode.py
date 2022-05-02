import random
from TextToSpeechManager import TextToSpeech
from MicrophoneManager import Mic

class MediumNode:
    hitPoints = 0
    numEnemy = 0
    sound = TextToSpeech()
    mic = Mic()

    def __init__(self):
        print('medium node created')
        self.numEnemy = random.randint(2,4)
        self.hitPoints = self.numEnemy*20
        print('enemy hitpoints: ' + str(self.hitPoints))


    def nodeAction(self, player):
        self.sound.CreateSound("enemy.mp3", 'this is a medium battle - there are ' + str(self.numEnemy) + ' enemies')
        self.sound.PlaySound("enemy.mp3")
        print('this is a medium battle - there are ' + str(self.numEnemy) + ' enemies')

        self.sound.CreateSound("player.mp3", 'player current health is ' + str(player.hp))
        self.sound.PlaySound("player.mp3")
        print('player current health is ' + str(player.hp))

        #user = input('run or fight: ')
        #start fight animation
        words = ''
        while words == '':
            words = self.mic.Listen()

        if('run' in words):
            print('trying to run away')
            chance = random.randint(1, 4)
            if(chance == 1):
                print('run failed, you must fight')
                self.sound.CreateSound("runFail.mp3", "You tried to run but failed, you must fight")
                self.sound.PlaySound("runFail.mp3")
                self.fight(player)
            else:
                #maybe run animation
                #stop fight animation
                print('successfully ran to new node')
                self.sound.CreateSound("runSuccess.mp3", "You successfully ran away!")
                self.sound.PlaySound("runSuccess.mp3")
                player.pX = random.randint(0,4)
                player.pY = random.randint(0,4)
                print('player new position is ' + str(player.pX) + ' ' + str(player.pY))
        elif('fight' in words):
            self.fight(player)

    def fight(self, player):
        if self.hitPoints > 0:
            hit = random.randint(0,20)
            print('enemy attacks ' + str(hit*self.numEnemy))
            player.takeDamage(hit*self.numEnemy)
            print('player hp is ' + str(player.hp))
            self.hitPoints -= player.attack()
            if(self.hitPoints > 0):
                print('enemy remaining hitpoints ' + str(self.hitPoints))
                if(self.hitPoints % 20 == 0):
                    self.numEnemy = self.hitPoints/20
                else:
                    self.numEnemy = self.hitPoints/20 + 1
            self.nodeAction(player)
        else:
            self.sound.CreateSound("win.mp3", "you beat the medium enemies, you got a health boost of 50")
            self.sound.PlaySound("win.mp3")
            player.healthBoost(50)
            print('you beat the enemy')