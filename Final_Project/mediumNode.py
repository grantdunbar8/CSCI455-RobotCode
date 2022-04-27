class MediumNode:
    hitpoints = 60
    def __init__(self):
        print('medium node created')

    def nodeAction(self):
        print('this is a medium battle')
        print('hitpoint remaining' + self.hitpoints)
