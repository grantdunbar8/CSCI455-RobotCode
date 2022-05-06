
from MicrophoneManager import Mic
from TextToSpeechManager import TextToSpeech
from time import sleep
from kivy.app import App
#from AnimationManager import WindowApp, Talking, TakeDamage
from kivy.clock import Clock
import threading, _thread



class StartNode:
    def __init__(self):
        self.sound = TextToSpeech()
        #self.window = Talking()
        #self.actionRunning = True
        print('start node created')

    def firstThread(self):
        self.sound.CreateSound("startNode.mp3", "Welcome to the game!")
        
        self.sound.PlaySound("startNode.mp3")
        self.actionRunning = False

    def secondThread(self):

        while not self.actionRunning:
            self.window.run()



    def nodeAction(self, player):
        print('this is the start node')
        self.sound.CreateSound("startNode.mp3", "Welcome to the game!")
        
        self.sound.PlaySound("startNode.mp3")
        
        #start node animation

#window = Talking()
#window.run()
