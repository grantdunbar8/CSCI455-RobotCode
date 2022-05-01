import random
from operator import contains
from node import *
from player import Player
from MicrophoneManager import Mic
from TextToSpeechManager import TextToSpeech

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


player = Player()
mic = Mic()
sound = TextToSpeech()

#make start and finish node
sx = 0
sy = 0
fx = 0
fy = 0
start = random.randint(1,4)
if(start == 1):
    #west wall
    sx = 0
    sy = random.randint(0,4)
    fx = 4
    fy = random.randint(0,4)

elif(start == 2):
    #north wall
    sx = random.randint(0,4)
    sy = 0
    fx = random.randint(0,4)
    fy = 4

elif(start == 3):
    #east wall
    sx = 4
    sy = random.randint(0,4)
    fx = 0
    fy = random.randint(0,4)

else:
    #south wall
    sx = random.randint(0,4)
    sy = 4
    fx = random.randint(0,4)
    fy = 0

map[sx][sy].setState('start')
map[fx][fy].setState('finish')
player.pX = sx
player.pY = sy

#make charging stations
def chargeOne(map):
    cx = random.randint(0,2)
    cy = random.randint(0,2)
    if((cx == 0 or cx == 2) and cy == 2 ):
        cy = random.randint(0,1)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('charging')
        return True
    else:
        return False

def chargeTwo(map):
    cx = random.randint(0,2)
    cy = random.randint(3,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('charging')
        return True
    else:
        return False

def chargeThree(map):
    cx = random.randint(3,4)
    cy = random.randint(0,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('charging')
        return True
    else:
        return False

cOne = False
cTwo = False
cThree = False

while not cOne:
    cOne = chargeOne(map)

while not cTwo:
    cTwo = chargeTwo(map)

while not cThree:
    cThree = chargeThree(map)

#make coffee shops
def coffeeOne(map):
    cx = random.randint(0,1)
    cy = random.randint(0,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('coffee')
        return True
    else:
        return False
def coffeeTwo(map):
    cx = random.randint(3,4)
    cy = random.randint(0,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('coffee')
        return True
    else:
        return False

cOne = False
cTwo = False

while not cOne:
    cOne = coffeeOne(map)
while not cTwo:
    cTwo = coffeeTwo(map)

#make easy nodes
def easy(map):
    cx = random.randint(0,4)
    cy = random.randint(0,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('easy')
        return True
    else:
        return False

e1 = False
e2 = False
e3 = False
e4 = False
e5 = False
e6 = False

while not e1:
    e1 = easy(map)
while not e2:
    e2 = easy(map)
while not e3:
    e3 = easy(map)
while not e4:
    e4 = easy(map)
while not e5:
    e5 = easy(map)
while not e6:
    e6 = easy(map)

#make medium nodes
def medium(map):
    cx = random.randint(0,4)
    cy = random.randint(0,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('medium')
        return True
    else:
        return False

m1 = False
m2 = False
m3 = False
m4 = False
m5 = False

while not m1:
    m1 = medium(map)
while not m2:
    m2 = medium(map)
while not m3:
    m3 = medium(map)
while not m4:
    m4 = medium(map)
while not m5:
    m5 = medium(map)
 
#make hard nodes
def hard(map):
    cx = random.randint(0,4)
    cy = random.randint(0,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('hard')
        return True
    else:
        return False

h1 = False
h2 = False
h3 = False

while not h1:
    h1 = hard(map)
while not h2:
    h2 = hard(map)
while not h3:
    h3 = hard(map)

#make fun nodes
def fun(map):
    cx = random.randint(0,4)
    cy = random.randint(0,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('fun')
        return True
    else:
        return False    

f1 = False
f2 = False

while not f1:
    f1 = fun(map)
while not f2:
    f2 = fun(map)

#make tricky node
def tricky(map, player):
    cx = random.randint(0,4)
    cy = random.randint(0,4)
    if(map[cx][cy].isBlank()):
        map[cx][cy].setState('fun')
        player.kX = cx
        player.kY = cy
        return True
    else:
        return False 

t1 = False

while not t1:
    t1 = tricky(map, player)

print('all nodes have been initialized, 1 start, 1 finish, 3 recharge, 2 coffee, 6 easy, 5 medium, 3 hard, 2 fun, and 1 tricky')

user = ''
words = ''
while('exit' not in words):
    words = 'exit'
    
    currentPosition = map[player.pX][player.pY]
    currentPosition.runState(player)
    currentPosition = map[player.pX][player.pY]
    currentPosition.getDirections()
    words = mic.Listen()
    # if(type(words) is type(None)):
    #     words = 'something'
    print("GOT HERE: " + str(words) + "TYPE: " + str(type(words)))
    #user = input(':')
    if('west' in words):
        if(currentPosition.ableWest()):
            player.pX-=1
            player.moves+=1
            sound.CreateSound("goWest.mp3", "going west")
            sound.PlaySound("goWest.mp3")
            print("GOT HERE 2222")
            player.movePlayer('west')
            
            
        else:
            print('can not go that way')
    if('east' in words):
        if(currentPosition.ableEast()):
            player.pX+=1
            player.moves+=1
            sound.CreateSound("goEast.mp3", "going east")
            print(sound.PlaySound("goEast.mp3"))
            print("GOT HERE 2222")
            player.movePlayer('east')
            
            
        else:
            print('can not go that way')
    if('north' in words):
        if(currentPosition.ableNorth()):
            player.pY-=1
            player.moves+=1
            sound.CreateSound("goNorth.mp3", "going north")
            sound.PlaySound("goNorth.mp3")
            player.movePlayer('north')
        else:
            print('can not go that way')
    if('south' in words):
        if(currentPosition.ableSouth()):
            player.pY+=1
            player.moves+=1
            sound.CreateSound("goSouth.mp3", "going south")
            sound.PlaySound("goSouth.mp3")
            player.movePlayer('south')
        else:
            print('can not go that way')
    




# while(input != 'exit'):
#     currentPosition = map[player.pX][player.pY]
#     currentPosition.runState(player)
#     currentPosition = map[player.pX][player.pY]
#     currentPosition.getDirections()
#     user = input(':')
#     if(user == 'west'):
#         if(currentPosition.ableWest()):
#             player.pX-=1
#             player.moves+=1
#             player.movePlayer(user)
#         else:
#             print('can not go that way')
#     if(user == 'east'):
#         if(currentPosition.ableEast()):
#             player.pX+=1
#             player.moves+=1
#             player.movePlayer(user)
#         else:
#             print('can not go that way')
#     if(user == 'north'):
#         if(currentPosition.ableNorth()):
#             player.pY-=1
#             player.moves+=1
#             player.movePlayer(user)
#         else:
#             print('can not go that way')
#     if(user == 'south'):
#         if(currentPosition.ableSouth()):
#             player.pY+=1
#             player.moves+=1
#             player.movePlayer(user)
#         else:
#             print('can not go that way')
    





