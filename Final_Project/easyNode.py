import random
from TextToSpeechManager import TextToSpeech
from MicrophoneManager import Mic

class EasyNode:
    hitPoints = 0
    numEnemy = 0
    sound = TextToSpeech()
    mic = Mic()
    beenHere = False

    def __init__(self):
        print('easy node created')
        self.numEnemy = random.randint(3,6)
        self.hitPoints = self.numEnemy*10
        print('enemy hitpoints: ' + str(self.hitPoints))


    def nodeAction(self, player):
        if self.hitPoints > 0:
            #fight animation
            if not self.beenHere:
                self.sound.CreateSound("enemy.mp3", 'this is an easy battle - there are ' + str(self.numEnemy) + ' enemies')
            elif self.hitPoints > 0:
                self.sound.CreateSound("enemy.mp3", 'there are ' + str(self.numEnemy) + ' easy enemies remaining')
            
            self.sound.PlaySound("enemy.mp3")
            print('this is an easy battle - there are ' + str(self.numEnemy) + ' enemies')

            beenHere = True

            self.sound.CreateSound("player.mp3", 'player current health is ' + str(player.hp))
            self.sound.PlaySound("player.mp3")
            print('player current health is ' + str(player.hp))

            # Say what the toal HP of all living enemies is
            self.sound.CreateSound("totalHP.mp3", 'enemies combined health is ' + str(self.hitPoints))
            self.sound.PlaySound("totalHP.mp3")
            print('enemies combined health is ' + str(self.hitPoints))

            #user = input('run or fight: ')
            self.sound.CreateSound("runFight.mp3", "Do you want to run or fight?")
            self.sound.PlaySound("runFight.mp3")
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
            self.sound.CreateSound("beat.mp3", "You have already beat this easy enemy")
            self.sound.PlaySound("beat.mp3")

            # if(user == 'run'):
            #     print('trying to run away')
            #     chance = random.randint(1, 4)
            #     if(chance == 1):
            #         print('run failed, you must fight')
            #         self.fight(player)
            #     else:
            #         print('successfully ran to new node')
            #         player.pX = random.randint(0,4)
            #         player.pY = random.randint(0,4)
            #         print('player new position is ' + str(player.pX) + ' ' + str(player.pY))
            # else:
            #     self.fight(player)

    def fight(self, player):
        if self.hitPoints > 0:
            hit = random.randint(0,5)
            print('enemy attacks ' + str(hit*self.numEnemy))
            player.takeDamage(hit*self.numEnemy)

            # Say how much damage player took when hit
            self.sound.CreateSound("playerHit.mp3", "I have sustained " + str(hit*self.numEnemy) + " damage")
            self.sound.PlaySound("playerHit.mp3")
            
            print('player hp is ' + str(player.hp))
            
            playersAttack = player.attack()
            self.hitPoint -= playersAttack
            #self.hitPoints -= player.attack()

            # Say how much damage was dealt to the enemies
            self.sound.CreateSound("enemyHit.mp3", "I did " + str(playersAttack) + " damage to the enemies")
            
            if(self.hitPoints > 0):
                print('enemy remaining hitpoints ' + str(self.hitPoints))
                if(self.hitPoints % 10 == 0):
                    self.numEnemy = self.hitPoints/10
                    self.numEnemy = int(self.numEnemy)
                else:
                    self.numEnemy = self.hitPoints/10 + 1
                    self.numEnemy = int(self.numEnemy)
            self.nodeAction(player)
        else:
            self.sound.CreateSound("win.mp3", "you beat the easy ememies, you got a health boost of 20")
            self.sound.PlaySound("win.mp3")
            player.healthBoost(20)
            print('you beat the enemy')

    
