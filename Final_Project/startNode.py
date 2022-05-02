import imp
from pkgutil import ImpImporter
from MicrophoneManager import Mic
from TextToSpeechManager import TextToSpeech



class StartNode:
    def __init__(self):
        self.sound = TextToSpeech()
        print('start node created')

    def nodeAction(self, player):
        print('this is the start node')
        self.sound.CreateSound("startNode.mp3", "Welcome to the game!")
        self.sound.PlaySound("startNode.mp3")
        #start node animation