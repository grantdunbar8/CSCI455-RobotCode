class EasyNode:
    hitPoints = 30
    def __init__(self):
        print('easy node created')

    def nodeAction(self):
        print('this is an easy battle')
        print('remaining hitpoints' + self.hitPoints)