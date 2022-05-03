from TextToSpeechManager import TextToSpeech
from MicrophoneManager import Mic

class TrickyNode:
    def __init__(self):
        self.sound = TextToSpeech()
        self.mic = Mic()
        print('tricky node created')

    def nodeAction(self, player):
        print('this is the tricky node')
        self.sound.CreateSound("trickyNode.mp3", "You found a wizard, solve his riddle. What gets wetter as it dries?")
        self.sound.PlaySound("trickyNode.mp3")
        player.trickyMover()
        #user = input('what gets wetter as it dries? ')

        words = ''
        while words == '':
            words = self.mic.Listen()
        if 'towel' in words:
            print('you got the key')
            self.sound.CreateSound("trickyYes.mp3", "You are right! Here is the key!")
            self.sound.PlaySound("trickYes.mp3")
            player.gotKey()
        else:
            self.sound.CreateSound("trickyNo.mp3", "Nope, try again.")
            self.sound.PlaySound("trickNo.mp3")
            print('try again')
            self.nodeAction(player)
        #tricky node animation