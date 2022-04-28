class CoffeeNode:
    def __init__(self):
        print('coffee node created')

    def nodeAction(self, player):
        #coffe node animation
        print('the key is ' + player.hintDir() + ' from your current position')