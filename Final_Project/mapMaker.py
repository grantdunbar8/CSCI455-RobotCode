from node import *
from player import Player

map = []
col0 = [Node(False, True, False, False), Node(False, True, False, True), Node(False, False, True, True), Node(False, True, True, False), Node(False, True, False, False)]
col1 = [Node(True, True, False, True), Node(True, False, True, True), Node(False, True, True, False), Node(True, False, False, True), Node(True, True, True, False)]
col2 = [Node(True, False, False, True), Node(False, False, True, False), Node(True, True, False, False), Node(False, False, False, True), Node(True, False, True, False)]
col3 = [Node(False, True, False, False), Node(False, True, False, True), Node(True, False, True, True), Node(False, True, True, True), Node(False, True, True, False)]
col4 = [Node(True, False, False, True), Node(True, False, True, True), Node(False, False, True, True), Node(True, False, True, False), Node(True, False, False, False)]

map.append(col0)
map.append(col1)
map.append(col2)
map.append(col3)
map.append(col4)

x = 0
y = 0

map[0][0].setState('start')
map[1][0].setState('charging')
#map[1][0].setState('tricky')
map[1][1].setState('finish')

player = Player()


user = ''
while(input != 'exit'):
    currentPosition = map[x][y]
    currentPosition.runState(player)
    currentPosition.getDirections()
    user = input(':')
    if(user == 'west'):
        if(currentPosition.ableWest()):
            x-=1
        else:
            print('can not go that way')
    if(user == 'east'):
        if(currentPosition.ableEast()):
            x+=1
        else:
            print('can not go that way')
    if(user == 'north'):
        if(currentPosition.ableNorth()):
            y-=1
        else:
            print('can not go that way')
    if(user == 'south'):
        if(currentPosition.ableSouth()):
            y+=1
        else:
            print('can not go that way')




