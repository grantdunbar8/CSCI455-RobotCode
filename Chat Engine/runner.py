from rule import *
import random

file = open('testing1.txt', 'r')

lines = file.readlines()

rules = []
numLines = len(lines)

lSplit = []
uLevel = 0
userInput = ""
robotOutput = ""

print('*******PARSING HAS STARTED*********')

for line in lines:
    print("\n\n\n\nLINE: " + line)

    # Check if line is a comment
    if '#' not in line[0]:
        # Here if line was not a comment
        print("^ Line is not a comment\n\n")

        # Parse line into 3 sections: uLevel, userInput, and robotOutput
        lSplit = line.split(":")

        # Assign the parsed sections to their respective variables
        uString = lSplit[0]
        userInput = lSplit[1]
        robotOutput = lSplit[2]

        # Remove whitespace
        uString = "".join(uString.split())

        # Get integer uLevel
        uSplit = uString.split("u")
        if uSplit[1] == "":
            uLevel = 0
        else:
            uLevel = uSplit[1]

        # Handle user input
        if "[" not in lSplit[1]:
            parsedInput = []
            if "\"" in lSplit[1]:
                parsedInput = lSplit[2].split("\"")
                parsedInput.pop(0)
                parsedInput.pop(len(parsedOutput) - 1)
            else:
                parsedInput.append(lSplit[1])
            print("PARSED INPUT")
            print(parsedInput)
        else:
            # Parses into [thing1, thing2, thingx] form user input
            if "\"" in lSplit[1]:
                parsedInput = lSplit[2].split("[")[1].split("]")[0].split(" ")
                firstQuote = ""
                tempInput = []
                for i in range(len(parsedInput)):
                    if "\"" in parsedInput[i] and firstQuote == "":
                        firstQuote = parsedInput[i]
                    elif "\"" in parsedInput[i] and not firstQuote == "":
                        tempString = firstQuote + " " + parsedInput[i]
                        tempString = tempString.replace("\"", "")
                        tempOutput.append(tempString)
                    else:
                        tempOutput.append(parsedInput[i])
                parsedInput = tempOutput
                
            else:
                parsedInput = lSplit[1].split("[")[1].split("]")[0].split(" ")
            print("PARSED INPUT ELSE STATEMENT")
            print(parsedInput)

        # Handle robot output
        if "[" not in lSplit[2]:
            parsedOutput = []
            if "\"" in lSplit[2]:
                parsedOutput = lSplit[2].split("\"")
                parsedOutput.pop(0)
                parsedOutput.pop(len(parsedOutput) - 1)
            else:
                parsedOutput.append(lSplit[2].replace("\n", ""))
            print("PARSED OUTPUT")
            print(parsedOutput)
        else:
            # Parses into [thing1, thing2, thingx] form robot output
            if "\"" in lSplit[2]:
                parsedOutput = lSplit[2].split("[")[1].split("]")[0].split(" ")
                firstQuote = ""
                tempOutput = []
                for i in range(len(parsedOutput)):
                    if "\"" in parsedOutput[i] and firstQuote == "":
                        firstQuote = parsedOutput[i]
                    elif "\"" in parsedOutput[i] and not firstQuote == "":
                        tempString = firstQuote + " " + parsedOutput[i]
                        tempString = tempString.replace("\"", "")
                        tempOutput.append(tempString)
                    else:
                        tempOutput.append(parsedOutput[i])
                parsedOutput = tempOutput
                        
            else:
                parsedOutput = lSplit[2].split("[")[1].split("]")[0].split(" ")
            print("PARSED OUTPUT ELSE STATEMENT")
            print(parsedOutput)

        if uLevel == 0:
            # If the uLevel is equal to 0
            print("uLevel was 0")
            print(uLevel)
            rules.append(rule(uLevel, parsedInput, parsedOutput))
        else:
            # If the uLevel us not equal to 0
            print("uLevel was NOT 0")
            print(uLevel)
            holderRule = rules[len(rules)-1]
            for element in range(1, int(uLevel)):
                holderRule = holderRule.getLastChild()
            holderRule.addChild(rule(uLevel, parsedInput, parsedOutput))
    else:
        # Here if line was a comment
        print("^ Line is a comment\n\n")

file.close()
for x in range (0, len(rules)):
    rules[x].printFullArray(x)
print('Robot is listening')

lastCommand = True
foundRule = False

while(True):
    user = input(':')
    if(lastCommand == True):
        for Rule in rules:
            for inputOptions in Rule.userInput:
                if(inputOptions.split('(')[1].split(')')[0] == user):
                    randomInput = random.randint(0,len(Rule.robotOutput)-1) 
                    print(Rule.robotOutput[randomInput])
                    lastCommand = Rule
                    foundRule = True
            
    else:
        for Rule in lastCommand.children:
            # if str(Rule.userInput.split('(')[1].split(')')[0]) == str(user):
            #     randomInput = random.randint(0,len(Rule.robotOutput)-1) 
            #     print(Rule.robotOutput[randomInput])
            #     lastCommand = Rule
            #     foundRule = True
            for inputOptions in Rule.userInput:
                if(inputOptions.split('(')[1].split(')')[0] == user):
                    randomInput = random.randint(0,len(Rule.robotOutput)-1) 
                    print(Rule.robotOutput[randomInput])
                    lastCommand = Rule
                    foundRule = True
        
        if not foundRule:
            for Rule in rules:
                # test1 = str(Rule.userInput[0].split('(')[1].split(')')[0])
                # test2 = str(user)
                # if(test1 == test2):    
                #     randomInput = random.randint(0,len(Rule.robotOutput)-1) 
                #     print(Rule.robotOutput[randomInput])
                #     lastCommand = Rule
                #     foundRule = True
                for inputOptions in Rule.userInput:
                    if(inputOptions.split('(')[1].split(')')[0] == user):
                        randomInput = random.randint(0,len(Rule.robotOutput)-1) 
                        print(Rule.robotOutput[randomInput])
                        lastCommand = Rule
                        foundRule = True
        
    if(user == 'exit'):
        print('see ya')
        break

    if not foundRule:
        print('I do not know that phrase. Please enter a new one')
        lastCommand = True
        
    foundRule = False   