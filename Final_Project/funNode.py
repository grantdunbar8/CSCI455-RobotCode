class FunNode:
    beenVisited = False

    def __init__(self):
        print('fun node created')

    def nodeAction(self, player):
        #fun node animation
        print('this is the fun node')
        print('you better start dancing')
        if(player.totalHP != 150 and not self.beenVisited):
            print('hp boost')
            player.boostHealth()
            player.mover.boostMove()
        elif(not self.beenVisited):
            print('attack boost')
            player.boostAttack()
            player.mover.boostMove()
        else:
            print('you have already visited this fun node')