from Command import *

commands = [Command(0, 'head up', 7500), Command(0, 'waist right', 4500), Command(0, 'wait for', 'hello'), Command(1, 'pause', 0), Command(0, 'speak', 'i am a robot')]

for item in commands:
    item.ExecuteCommand()