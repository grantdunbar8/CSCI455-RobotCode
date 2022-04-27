class CoffeeNode:
    def __init__(self):
        print('coffee node created')

    def nodeAction(self, player):
        print('the key is ' + player.hintDir() + ' from your current position')