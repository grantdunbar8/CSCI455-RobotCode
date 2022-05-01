from startNode import StartNode
from finishNode import FinishNode
from chargingNode import ChargingNode
from coffeeNode import CoffeeNode
from easyNode import EasyNode
from mediumNode import MediumNode
from hardNode import HardNode
from funNode import FunNode
from trickyNode import TrickyNode
from blankNode import BlankNode
from TextToSpeechManager import TextToSpeech
import sys

class Node:
    west = ''
    east = ''
    north = ''
    south = ''
    state = BlankNode()
    stateType = ''
    sound = TextToSpeech()

    def __init__(self, west, east, north, south):
        self.west = west
        self.east = east
        self.north = north
        self.south = south

    def getDirections(self):
        self.sound.CreateSound("options.mp3", "you can go ")
        self.sound.PlaySound("options.mp3")
        print('you can go:')
        if(self.west):
            self.sound.CreateSound("west.mp3", "west")
            self.sound.PlaySound("west.mp3")
            print('west')
        if(self.east):
            self.sound.CreateSound("east.mp3", "east")
            self.sound.PlaySound("east.mp3")
            print('east')
        if(self.north):
            self.sound.CreateSound("north.mp3", "north")
            self.sound.PlaySound("north.mp3")
            print('north')
        if(self.south):
            self.sound.CreateSound("south.mp3", "south")
            self.sound.PlaySound("south.mp3")
            print('south')

    def ableWest(self):
        return self.west

    def ableEast(self):
        return self.east
    
    def ableNorth(self):
        return self.north
    
    def ableSouth(self):
        return self.south

    def isBlank(self):
        if self.stateType == '':
            return True
        else:
            return False

    def setState(self, state):
        if(state == 'start'):
            self.state = StartNode()
        elif(state == 'finish'):
            self.state = FinishNode()
        elif(state == 'charging'):
            self.state = ChargingNode()
        elif(state == 'coffee'):
            self.state = CoffeeNode()
        elif(state == 'easy'):
            self.state = EasyNode()
        elif(state == 'medium'):
            self.state = MediumNode()
        elif(state == 'hard'):
            self.state = HardNode()
        elif(state == 'fun'):
            self.state = FunNode()
        elif(state == 'tricky'):
            self.state = TrickyNode()
        self.stateType = state
    
    def runState(self, player):
        if(player.moves > 50):
            print('too many moves have been made, you lose')
            sys.exit(0)
        
        self.state.nodeAction(player)
    