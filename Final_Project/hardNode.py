class HardNode:
    hitpoints = 90
    def __init__(self):
        print('hard node created')

    def nodeAction(self):
        print('this is the boss fight')
        print('hitpoints remaining' + self.hitpoints)