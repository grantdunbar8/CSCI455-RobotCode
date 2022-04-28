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

#randomize here
map[0][0].setState('start')
map[1][0].setState('hard')
#map[1][0].setState('tricky')
map[1][1].setState('finish')

player = Player()


user = ''
while(input != 'exit'):
    currentPosition = map[player.pX][player.pY]
    currentPosition.runState(player)
    currentPosition = map[player.pX][player.pY]
    currentPosition.getDirections()
    user = input(':')
    if(user == 'west'):
        if(currentPosition.ableWest()):
            player.pX-=1
            player.moves+=1
            player.movePlayer(user)
        else:
            print('can not go that way')
    if(user == 'east'):
        if(currentPosition.ableEast()):
            player.pX+=1
            player.moves+=1
            player.movePlayer(user)
        else:
            print('can not go that way')
    if(user == 'north'):
        if(currentPosition.ableNorth()):
            player.pY-=1
            player.moves+=1
            player.movePlayer(user)
        else:
            print('can not go that way')
    if(user == 'south'):
        if(currentPosition.ableSouth()):
            player.pY+=1
            player.moves+=1
            player.movePlayer(user)
        else:
            print('can not go that way')
    





