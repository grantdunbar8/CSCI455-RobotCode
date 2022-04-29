class TrickyNode:
    def __init__(self):
        print('tricky node created')

    def nodeAction(self, player):
        print('this is the tricky node')
        user = input('what gets wetter as it dries? ')
        if input == 'towel':
            print('you got the key')
            player.gotKey()
        else:
            print('try again')
            self.nodeAction(player)
        #tricky node animation