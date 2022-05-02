import random
from TextToSpeechManager import TextToSpeech
from MicrophoneManager import Mic

class HardNode:
    hitPoints = 0
    sound = TextToSpeech()
    mic = Mic()
    beenHere = False

    def __init__(self):
        print('boss node created')
        self.hitPoints = random.randint(80,120)
        print('enemy hitpoints: ' + str(self.hitPoints))


    def nodeAction(self, player):
        if(self.hitPoints > 0):
            #boss fight animation
            self.sound.CreateSound("enemy.mp3", "this is a boss battle")
            self.sound.PlaySound("enemy.mp3")
            print('this is a boss battle')

            self.sound.CreateSound("player.mp3", 'player current health is ' + str(player.hp))
            self.sound.PlaySound("player.mp3")
            print('player current health is ' + str(player.hp))
            
            #user = input('run or fight: ')
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
                    print('successfully ran to new node')
                    self.sound.CreateSound("runSuccess.mp3", "You successfully ran away!")
                    self.sound.PlaySound("runSuccess.mp3")
                    player.pX = random.randint(0,4)
                    player.pY = random.randint(0,4)
                    print('player new position is ' + str(player.pX) + ' ' + str(player.pY))
            elif('fight' in words):
                self.fight(player)
        else:
            self.sound.CreateSound("beat.mp3", "You have already conquered this boss")
            self.sound.PlaySound("beat.mp3")

    def fight(self, player):
        if self.hitPoints > 0:
            hit = random.randint(0,50)
            print('enemy attacks ' + str(hit))
            player.takeDamage(hit)
            print('player hp is ' + str(player.hp))
            self.hitPoints -= player.attack()
            if(self.hitPoints > 0):
                print('enemy remaining hitpoints ' + str(self.hitPoints))
            self.nodeAction(player)
        else:
            self.sound.CreateSound("win.mp3", "congradulations, you beat the boss, you got a health boost of 80")
            self.sound.PlaySound("win.mp3")
            player.healthBoost(80)
            print('you beat the BOSS')