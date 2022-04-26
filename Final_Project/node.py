class Node:
    west = ''
    east = ''
    north = ''
    south = ''
    state = ''

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
    