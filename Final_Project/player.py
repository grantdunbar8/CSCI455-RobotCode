import random, sys
from movingTester import MoveTester

class Player:
    totalHP = 100
    hp = 100
    direction = 'east'
    regularAttack = 20
    critAttack = 40
    hasKey = False
    moves = 0
    mover = MoveTester()

    kX = 4
    kY = 4
    pX = 0
    pY = 0
    
    #TODO: should be able to put all movements NOT animations in the player class
    #   animations are for each node not interactions within the node, unless we want to change that

    def __init__(self):
        print('player has been created')
        print('current health is: ' + str(self.hp))
        self.mover = MoveTester()

    def attack(self):
        attack = random.randint(1,10)
        if attack == 0:
            print('missed attack')
            #miss animation
            #miss movement
            self.mover.armMissAttack()
                     
            return 0
        elif attack == 10:
            print('crit attack')
            #crit attack animation
            #crit movement
            self.mover.armCritAttack()

            return self.critAttack
        else:
            print('normal attack')
            #attack animation
            #normal movement
            self.mover.armDefaultAttack()

            return self.regularAttack
    
    def takeDamage(self, damage):
        self.hp -= damage
        #take damage animation
        #take damage movement
        self.mover.takeDamage()

        if(self.hp <= 0):
            print('you died')
            sys.exit(0)

    def boostHealth(self):
        self.totalHP += 50
        self.hp += 50
        self.mover.boostMove()
    
    def boostAttack(self):
        self.regularAttack += 10
        self.critAttack += 10
        self.mover.boostMove()

    def recharge(self):
        self.hp = self.totalHP
        self.mover.rechargeMove()

    def key(self):
        return self.hasKey

    def gotKey(self):
        self.hasKey = True

    def healthBoost(self, boost):
        if(self.hp + boost > self.totalHP):
            self.hp = self.totalHP
        else:
            self.hp+=boost

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

    def movePlayer(self, directionChoice):
        #check direction of robot
        if(directionChoice == self.direction):
            self.mover.MoveToNextNode()
        else:
            while(directionChoice != self.direction):   #while robot isn't facing the right way
                if(directionChoice == 'east'):
                    if(self.direction == 'north'):
                        self.mover.TurnRight()
                        self.direction = 'east'
                    elif(self.direction == 'west'):
                        self.mover.TurnRight()
                        self.mover.TurnRight()
                        self.direction = 'east'
                    elif(self.direction == 'south'):
                        self.mover.TurnLeft()
                        self.direction = 'east'

                elif(directionChoice == 'north'):
                    if(self.direction == 'east'):
                        self.mover.TurnLeft()
                        self.direction = 'north'
                    elif(self.direction == 'west'):
                        self.mover.TurnRight()
                        self.direction = 'north'
                    elif(self.direction == 'south'):
                        self.mover.TurnRight()
                        self.mover.TurnRight()
                        self.direction = 'north'

                elif(directionChoice == 'west'):
                    if(self.direction == 'north'):
                        self.mover.TurnLeft()
                        self.direction = 'west'
                    elif(self.direction == 'east'):
                        self.mover.TurnRight()
                        self.mover.TurnRight()
                        self.direction = 'west'
                    elif(self.direction == 'south'):
                        self.mover.TurnRight()
                        self.direction = 'west'

                elif(directionChoice == 'south'):
                    if(self.direction == 'north'):
                        self.mover.TurnRight()
                        self.mover.TurnRight()
                        self.direction = 'south'
                    elif(self.direction == 'east'):
                        self.mover.TurnRight()
                        self.direction = 'south'
                    elif(self.direction == 'west'):
                        self.mover.TurnLeft()
                        self.direction = 'south'
            #move robot to next node once facing the right way
            self.mover.MoveToNextNode()


        #make robot turn that direction
        #make robot go forward 
        print()