import random, sys
class Player:
    totalHP = 100
    hp = 100
    direction = 'east'
    regularAttack = 20
    critAttack = 40
    hasKey = False
    moves = 0

    kX = 4
    kY = 4
    pX = 0
    pY = 0
    
    def __init__(self):
        print('player has been created')
        print('current health is: ' + str(self.hp))

    def attack(self):
        attack = random.randint(1,10)
        if attack == 0:
            print('missed attack')
            return 0
        elif attack == 10:
            print('crit attack')
            return self.critAttack
        else:
            print('normal attack')
            return self.regularAttack
    
    def takeDamage(self, damage):
        self.hp -= damage
        if(self.hp <= 0):
            print('you died')
            sys.exit(0)

    def boostHealth(self):
        self.totalHP += 50
        self.hp += 50
    
    def boostAttack(self):
        self.regularAttack += 10
        self.critAttack += 10

    def recharge(self):
        self.hp = self.totalHP

    def key(self):
        return self.hasKey

    def gotKey(self):
        self.hasKey = True

    def hintDir(self):
        if(self.pX == self.kX and self.pY < self.kY):
            return('south')
        elif(self.pX == self.kX and self.pY > self.kY):
            return('north')
        elif(self.pX > self.kX and self.pY == self.kY):
            return('west')
        elif(self.pX < self.kX and self.pY == self.kY):
            return('east')
        elif(self.pX < self.kX and self.pY > self.kY):
            return('northeast')
        elif(self.pX > self.kX and self.pY > self.kY):
            return('northwest')
        elif(self.pX < self.kX and self.pY < self.kY):
            return('southeast')
        elif(self.pX > self.kX and self.pY < self.kY):
            return('southwest')