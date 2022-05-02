from TextToSpeechManager import TextToSpeech


class FunNode:
    beenVisited = False

    def __init__(self):
        self.sound = TextToSpeech()
        print('fun node created')

    def nodeAction(self, player):
        #fun node animation
        self.sound.CreateSound("funNode.mp3", "You've reached a fun node")
        self.sound.PlaySound("funNode.mp3")
        print('this is the fun node')
        print('you better start dancing')
        if(player.totalHP != 150 and not self.beenVisited):
            print('hp boost')
            self.sound.CreateSound("hpBoost.mp3", "You got an HP boost!")
            self.sound.PlaySound("hpBoost.mp3")
            player.boostHealth()
            #player.mover.boostMove()
            self.beenVisited = True
        elif(not self.beenVisited):
            print('attack boost')
            self.sound.CreateSound("attBoost.mp3", "You got and attack power boost!")
            self.sound.PlaySound("attBoost.mp3")
            player.boostAttack()
            #player.mover.boostMove()
            self.beenVisited = True
        else:
            print('you have already visited this fun node')
            self.sound.CreateSound("alreadyHere.mp3", "You've already been here")
            self.sound.PlaySound("alreadyHere.mp3")