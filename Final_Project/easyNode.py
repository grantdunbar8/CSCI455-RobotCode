import random
class EasyNode:
    hitPoints = 0
    numEnemy = 0
    def __init__(self):
        print('easy node created')
        self.numEnemy = random.randint(3,6)
        self.hitPoints = self.numEnemy*10
        print('enemy hitpoints: ' + str(self.hitPoints))


    def nodeAction(self, player):
        #fight animation
        self.sound.CreateSound("enemy.mp3", 'this is an easy battle - there are ' + str(self.numEnemy) + ' enemies')
        self.sound.PlaySound("enemy.mp3")
        print('this is an easy battle - there are ' + str(self.numEnemy) + ' enemies')

        self.sound.CreateSound("player.mp3", 'player current health is ' + str(player.hp))
        self.sound.PlaySound("player.mp3")
        print('player current health is ' + str(player.hp))
        user = input('run or fight: ')
        if(user == 'run'):
            print('trying to run away')
            chance = random.randint(1, 4)
            if(chance == 1):
                print('run failed, you must fight')
                self.fight(player)
            else:
                print('successfully ran to new node')
                player.pX = random.randint(0,4)
                player.pY = random.randint(0,4)
                print('player new position is ' + str(player.pX) + ' ' + str(player.pY))
        else:
            self.fight(player)

    def fight(self, player):
        if self.hitPoints > 0:
            hit = random.randint(0,5)
            print('enemy attacks ' + str(hit*self.numEnemy))
            player.takeDamage(hit*self.numEnemy)
            print('player hp is ' + str(player.hp))
            self.hitPoints -= player.attack()
            if(self.hitPoints > 0):
                print('enemy remaining hitpoints ' + str(self.hitPoints))
                if(self.hitPoints % 10 == 0):
                    self.numEnemy = self.hitPoints/10
                else:
                    self.numEnemy = self.hitPoints/10 + 1
                self.nodeAction(player)
        else:
            self.sound.CreateSound("win.mp3", "you beat the easy ememies, you got a health boost of 20")
            self.sound.PlaySound("win.mp3")
            player.healthBoost(20)
            print('you beat the enemy')

    