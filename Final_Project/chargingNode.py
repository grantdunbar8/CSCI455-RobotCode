class ChargingNode:
    beenVisited = False
    def __init__(self):
        print('charging node created')

    def nodeAction(self, player):
        if(not self.beenVisited):
            #charging node animation
            player.recharge()
            print('you are recharged!')
            self.beenVisited = True
            
        else:
            print('you have already been recharged here')