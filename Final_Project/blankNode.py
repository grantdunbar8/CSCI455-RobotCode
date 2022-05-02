from TextToSpeechManager import TextToSpeech


class BlankNode:
    def __init__(self):
        blank = 'blank'
        self.sound = TextToSpeech()
    
    def nodeAction(self, player):
        self.sound.CreateSound("blank.mp3", "There is nothing here, move along")
        self.sound.PlaySound("blank.mp3")
        print('this is a blank node, you are lucky')