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
import sys

class Node:
    west = ''
    east = ''
    north = ''
    south = ''
    state = BlankNode()

    def __init__(self, west, east, north, south):
        self.west = west
        self.east = east
        self.north = north
        self.south = south

    def getDirections(self):
        print('you can go:')
        if(self.west):
            print('west')
        if(self.east):
            print('east')
        if(self.north):
            print('north')
        if(self.south):
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
        if self.state == BlankNode():
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
    
    def runState(self, player):
        if(player.moves > 50):
            print('too many moves have been made, you lose')
            sys.exit(0)
        
        self.state.nodeAction(player)
    