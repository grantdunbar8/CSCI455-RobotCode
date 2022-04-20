from Command import *

commands = [Command(2, 'move forward', 0), Command(5, 'move backward', 0), Command(0, 'speak', 'hello world'), Command(0, 'wait for', 'you a hoe')]

for item in commands:
    item.ExecuteCommand()