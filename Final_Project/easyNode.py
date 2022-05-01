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
        print('this is an easy battle - there are ' + str(self.numEnemy) + ' enemies')
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
            self.nodeAction(player)
        print('you beat the enemy')

    