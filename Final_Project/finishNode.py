import sys
from TextToSpeechManager import TextToSpeech


class FinishNode:
    def __init__(self):
        self.sound = TextToSpeech()
        print('finish node created')

    def nodeAction(self, player):
        #finish node animation
        print('do you have the key?')
        self.sound.CreateSound("win1.mp3", "You've reached the finish, do you have the key?")
        self.sound.PlaySound("win1.mp3")
        if(player.key()):
            print('you win!')
            self.sound.CreateSound("win.mp3", "Congrats, you have won the game!")
            self.sound.PlaySound("win.mp3")
            sys.exit(0)
        else:
            print('you need to find the key')
            self.sound.CreateSound("notWin.mp3", "Come back when you have the key")
            self.sound.PlaySound("notWin.mp3")
            