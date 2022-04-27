import sys
class FinishNode:
    def __init__(self):
        print('finish node created')

    def nodeAction(self, player):
        print('do you have the key?')
        if(player.key()):
            print('you win!')
            sys.exit(0)
        else:
            print('you need to find the key')
            