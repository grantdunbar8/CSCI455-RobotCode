from TextToSpeechManager import TextToSpeech


class CoffeeNode:
    def __init__(self):
        self.sound = TextToSpeech()
        print('coffee node created')

    def nodeAction(self, player):
        #coffe node animation
        self.sound.CreateSound("coffee1.mp3", "You've reached a coffe node")
        self.sound.PlaySound("coffee1.mp3")
        self.sound.CreateSound("coffee.mp3", "They key is " + str(player.hintDir()) + " from your current position")
        self.sound.PlaySound("coffee.mp3")
        print('the key is ' + player.hintDir() + ' from your current position')