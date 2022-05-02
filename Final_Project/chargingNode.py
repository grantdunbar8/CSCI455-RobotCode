from TextToSpeechManager import TextToSpeech


class ChargingNode:
    beenVisited = False
    def __init__(self):
        self.sound = TextToSpeech()
        print('charging node created')

    def nodeAction(self, player):
        if(not self.beenVisited):
            #charging node animation

            self.sound.CreateSound("recharge1.mp3", "You've reached a recharge node")
            self.sound.PlaySound("recharge1.mp3")
            player.recharge()
            self.sound.CreateSound("recharge.mp3", "Your health has been recharged!")
            self.sound.PlaySound("recharge.mp3")
            
            print('you are recharged!')
            self.beenVisited = True
            
        else:
            self.sound.CreateSound("alreadyCharged.mp3", "You have already recharged here")
            self.sound.PlaySound("alreadyCharged.mp3")
            print('you have already been recharged here')