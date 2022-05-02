from TextToSpeechManager import TextToSpeech


class TrickyNode:
    def __init__(self):
        self.sound = TextToSpeech()
        print('tricky node created')

    def nodeAction(self, player):
        print('this is the tricky node')
        self.sound.CreateSound("trickyNode.mp3", "You found a wizard, solve his riddle")
        self.sound.PlaySound("trickyNode.mp3")
        user = input('what gets wetter as it dries? ')
        if input == 'towel':
            print('you got the key')
            player.gotKey()
        else:
            print('try again')
            self.nodeAction(player)
        #tricky node animation