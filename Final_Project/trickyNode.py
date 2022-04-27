class TrickyNode:
    def __init__(self):
        print('tricky node created')

    def nodeAction(self, player):
        print('this is the tricky node')
        print('you got the key')
        player.gotKey()