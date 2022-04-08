from rule import *
import random

file = open('testing2.txt', 'r')

lines = file.readlines()

rules = []
numLines = len(lines)

lSplit = []
uLevel = 0
userInput = ""
robotOutput = ""
definitions = ""
variables = []
variables2 = []

#print('*******PARSING HAS STARTED*********')

for line in lines:
    #print("\n\n\n\nLINE: " + line)

    # Check if line is a comment
    if '#' not in line:
        # Here if line was not a comment
        #print("^ Line is not a comment\n\n")

        #Define definitions
        if '~' in line[0]: 
            lSplit = line.split(":")
            definitions = lSplit[1]
            #print("DEF: " + definitions)
        else:
            # Parse line into 3 sections: uLevel, userInput, and robotOutput
            lSplit = line.split(":")
            # for each in lSplit:
            #     print("LINEEEEE:" + each)

            # Assign the parsed sections to their respective variables
            if(len(lSplit) != 3):
                print(line)
                print("ERROR: Unable to parse line")
                break
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
            lSplit[1] = lSplit[1].strip()
            lSplit[1] = lSplit[1].replace("(", "")
            lSplit[1] = lSplit[1].replace(")", "")

            #replaces ~greetings with list of options
            if(lSplit[1] == '~greetings'):
                #print("GOT INSIDE HERE>>>")
                lSplit[1] = definitions


            if "[" not in lSplit[1]:
                parsedInput = []
                if "\"" in lSplit[1]:
                    parsedInput = lSplit[2].split("\"")
                    parsedInput.pop(0)
                    parsedInput.pop(len(parsedOutput) - 1)
                else:
                    parsedInput.append(lSplit[1])
                #print("PARSED INPUT")
                #print(parsedInput)
            else:
                # Parses into [thing1, thing2, thingx] form user input
                parsedInput = []
                if "\"" in lSplit[1]:
                    parsedInput = lSplit[1].split("[")[1].split("]")[0].split(" ")

                    firstQuote = ""
                    tempInput = []
                    for i in range(len(parsedInput)):
                        if "\"" in parsedInput[i] and firstQuote == "":
                            firstQuote = parsedInput[i]
                        elif "\"" not in parsedInput[i] and not firstQuote == "":
                            firstQuote += ' ' + parsedInput[i]
                        elif "\"" in parsedInput[i] and not firstQuote == "":
                            tempString = firstQuote + " " + parsedInput[i]
                            tempString = tempString.replace("\"", "")
                            tempInput.append(tempString)
                        else:
                            tempInput.append(parsedInput[i])
                    parsedInput = tempInput
                    
                else:
                    parsedInput = lSplit[1].split("[")[1].split("]")[0].split(" ")
                #print("PARSED INPUT ELSE STATEMENT")
                #print(parsedInput)

            # Handle robot output

            #replaces ~greetings with list of options
            lSplit[2].replace(" ", "")
            lSplit[2].replace("\n", "")
            if('~' in lSplit[2]):
                lSplit[2] = definitions

            if "[" not in lSplit[2]:
                parsedOutput = []
                if "\"" in lSplit[2]:
                    parsedOutput = lSplit[2].split("\"")
                    parsedOutput.pop(0)
                    parsedOutput.pop(len(parsedOutput) - 1)
                elif('$' in lSplit[2]):
                    useOnce = lSplit[2].split()
                    for x in range(len(useOnce)):
                        if('$' in useOnce[x]):
                            if(useOnce[x] not in variables):
                                variables.append(useOnce[x])
                                variables.append('')
                    parsedOutput.append(lSplit[2].replace("\n", ""))
                else:
                    parsedOutput.append(lSplit[2].replace("\n", ""))
                #print("PARSED OUTPUT")
                #print(parsedOutput)
            else:
                # Parses into [thing1, thing2, thingx] form robot output
                if "\"" in lSplit[2]:
                    parsedOutput = lSplit[2].split("[")[1].split("]")[0].split(" ")
                    firstQuote = ""
                    tempOutput = []
                    for i in range(len(parsedOutput)):
                        if "\"" in parsedOutput[i] and firstQuote == "":
                            firstQuote = parsedOutput[i]
                        elif "\"" not in parsedOutput[i] and not firstQuote == "":
                            firstQuote += " " + parsedOutput[i]
                        elif "\"" in parsedOutput[i] and not firstQuote == "":
                            tempString = firstQuote + " " + parsedOutput[i]
                            tempString = tempString.replace("\"", "")
                            tempOutput.append(tempString)
                        else:
                            tempOutput.append(parsedOutput[i])
                    parsedOutput = tempOutput
                            
                else:
                    parsedOutput = lSplit[2].split("[")[1].split("]")[0].split(" ")
                #print("PARSED OUTPUT ELSE STATEMENT")
                #print(parsedOutput)

            if uLevel == 0:
                # If the uLevel is equal to 0
                #print("uLevel was 0")
                #print(uLevel)
                rules.append(rule(uLevel, parsedInput, parsedOutput))
            else:
                # If the uLevel us not equal to 0
                #print("uLevel was NOT 0")
                #print(uLevel)
                holderRule = rules[len(rules)-1]
                for element in range(1, int(uLevel)):
                    holderRule = holderRule.getLastChild()
                holderRule.addChild(rule(uLevel, parsedInput, parsedOutput))
    #else:
        # Here if line was a comment
        #print("^ Line is a comment\n\n")

file.close()
# for x in range (0, len(rules)):
#     rules[x].printFullArray(x)
print('Robot is listening')

lastCommand = True
foundRule = False
#builder = ""

while(True):
    user = input(':')
    if(lastCommand == True):
        for Rule in rules:
            for inputOptions in Rule.userInput: 
                option = inputOptions
                user.replace("\"", "")
                #if(inputOptions.split('(')[1].split(')')[0] == user):
                if(option == user):
                    randomInput = random.randint(0,len(Rule.robotOutput)-1)
                    #print("NO VARRRRRRRRRR")
                    if ('$' in Rule.robotOutput[randomInput]):
                            thisOutput = Rule.robotOutput[randomInput].split()
                            tempVariable = 'none'
                            numCounter = ''
                            for x in range(len(thisOutput)):
                                if('$' in thisOutput[x]):
                                    tempVariable = thisOutput[x]
                                    numCounter = x
                            for x in range(len(variables)):
                                if(tempVariable == variables[x]):
                                    thisOutput[numCounter] = variables[x+1]
                                    tempVariable = "none"
                            builder = ''
                            for each in thisOutput:
                                builder = builder + each + " "
                            print(builder)
                            lastCommand = Rule
                            foundRule = True
                    else:
                        print(Rule.robotOutput[randomInput])
                        lastCommand = Rule
                        foundRule = True
            
                
                inputOptionWords = option.split()
                inputUserWords = user.split()    
                if(('_' in inputOptionWords) and (len(inputOptionWords) == len(inputUserWords))):
                    #print(Rule.robotOutput)
                    for x in range(len(inputOptionWords)):
                        if((inputOptionWords[x] == inputUserWords[x]) or inputOptionWords[x] == '_'):
                            #print("Words Match")
                            #print(inputOptionWords)
                            if(inputOptionWords[x] == '_'):
                                #print("THERE IS ONE")
                                newVariable = inputUserWords[x]
                                thisOutput = Rule.robotOutput[0].split()
                                tempVariable = "none"
                                for each in thisOutput:
                                    if('$' in each):
                                        tempVariable = each
                                for y in range(len(variables)):
                                    if (variables[y] == tempVariable):
                                        #print(y)
                                        #print(variables)
                                        variables[y+1] = newVariable
                                        tempVariable = "none"
                            
                                #print(variables)
                                #print(thisOutput)

                                for y in range(len(thisOutput)):
                                    if('$' in thisOutput[y]):
                                        #print("===================")
                                        #print(Rule.robotOutput[0])
                                        thisOutput[y] = inputUserWords[x]
                                        builder = ""
                                        for i in thisOutput:
                                            builder = builder + i + " "
                                        #Rule.robotOutput = builder
                                        print(builder)
                                        #print("=================")
                                        #print(variables)
                                        lastCommand = Rule
                                        foundRule = True
                        else:
                            break


            
    else:
        for Rule in lastCommand.children:
            # if str(Rule.userInput.split('(')[1].split(')')[0]) == str(user):
            #     randomInput = random.randint(0,len(Rule.robotOutput)-1) 
            #     print(Rule.robotOutput[randomInput])
            #     lastCommand = Rule
            #     foundRule = True
            for inputOptions in Rule.userInput:
                option = inputOptions
                user.replace("\"", "")
                #if(inputOptions.split('(')[1].split(')')[0] == user):
                if(option == user):
                    randomInput = random.randint(0,len(Rule.robotOutput)-1) 
                    #print("NO VAR BUT THERE IS ONE2222")
                    if ('$' in Rule.robotOutput[randomInput]):
                        thisOutput = Rule.robotOutput[randomInput].split()
                        tempVariable = 'none'
                        numCounter = ''
                        for x in range(len(thisOutput)):
                            if('$' in thisOutput[x]):
                                tempVariable = thisOutput[x]
                                numCounter = x
                        for x in range(len(variables)):
                            if(tempVariable == variables[x]):
                                thisOutput[numCounter] = variables[x+1]
                                tempVariable = "none"
                        builder = ''
                        for each in thisOutput:
                            builder = builder + each + " "
                        print(builder)
                        lastCommand = Rule
                        foundRule = True
                    else:
                        print(Rule.robotOutput[randomInput])
                        lastCommand = Rule
                        foundRule = True

                inputOptionWords = option.split()
                inputUserWords = user.split()    
                if(('_' in inputOptionWords) and (len(inputOptionWords) == len(inputUserWords))):
                    
                    for x in range(len(inputOptionWords)):
                        if((inputOptionWords[x] == inputUserWords[x]) or inputOptionWords[x] == '_'):
                            #print("Words Match2")
                            if(inputOptionWords[x] == '_'):
                                newVariable = inputUserWords[x]
                                thisOutput = Rule.robotOutput[0].split()
                                #print(thisOutput)
                                tempVariable = "none"
                                for each in thisOutput:
                                    if('$' in each):
                                        tempVariable = each
                                for y in range(len(variables)):
                                    if (variables[y] == tempVariable):
                                        #print(y)
                                        #print(variables)
                                        variables[y+1] = newVariable
                                        tempVariable = "none"

                                for y in range(len(thisOutput)):
                                    if('$' in thisOutput[y]):
                                        thisOutput[y] = inputUserWords[x]
                                        builder = ""
                                        for i in thisOutput:
                                            builder = builder + i + " "
                                        #Rule.robotOutput = builder
                                        print(builder)
                                        lastCommand = Rule
                                        foundRule = True
                        else:
                            break
        
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
                    option = inputOptions
                    user.replace("\"", "")
                    #if(inputOptions.split('(')[1].split(')')[0] == user):
                    if(option == user):
                        randomInput = random.randint(0,len(Rule.robotOutput)-1) 
                        #print("ABCJDLSFKJSDLKFJSLDKFJSLDKFJSDLFKJSDLKFJSLDKFJLSDKJFLSKDJFLSDKFJ")
                        if ('$' in Rule.robotOutput[randomInput]):
                            thisOutput = Rule.robotOutput[randomInput].split()
                            tempVariable = 'none'
                            numCounter = ''
                            for x in range(len(thisOutput)):
                                if('$' in thisOutput[x]):
                                    tempVariable = thisOutput[x]
                                    numCounter = x
                            for x in range(len(variables)):
                                if(tempVariable == variables[x]):
                                    thisOutput[numCounter] = variables[x+1]
                                    tempVariable = "none"
                            builder = ''
                            for each in thisOutput:
                                builder = builder + each + " "
                            print(builder)
                            lastCommand = Rule
                            foundRule = True
                        else:
                            print(Rule.robotOutput[randomInput])
                            lastCommand = Rule
                            foundRule = True

                    inputOptionWords = option.split()
                    inputUserWords = user.split()    
                    if(('_' in inputOptionWords) and (len(inputOptionWords) == len(inputUserWords))):
                        
                        for x in range(len(inputOptionWords)):
                            if((inputOptionWords[x] == inputUserWords[x]) or inputOptionWords[x] == '_'):
                                #print("Words Match3")
                                if(inputOptionWords[x] == '_'):
                                    #print("GOT HERE LOL")
                                    newVariable = inputUserWords[x]
                                    #print(Rule.robotOutput)
                                    thisOutput = Rule.robotOutput[0].split()
                                    #print(thisOutput)
                                    tempVariable = "none"
                                    for each in thisOutput:
                                        if('$' in each):
                                            tempVariable = each
                                    for y in range(len(variables)):
                                        if (variables[y] == tempVariable):
                                            #print(y)
                                            #print(variables)
                                            variables[y+1] = newVariable
                                            tempVariable = "none"

                                    for y in range(len(thisOutput)):
                                        if('$' in thisOutput[y]):
                                            thisOutput[y] = inputUserWords[x]
                                            builder = ""
                                            for i in thisOutput:
                                                builder = builder + i + " "
                                            #Rule.robotOutput = builder
                                            print(builder)
                                            lastCommand = Rule
                                            foundRule = True
                            else:
                                break
        
    if(user == 'exit'):
        print('see ya')
        break

    if not foundRule:
        print('I do not know that phrase. Please enter a new one')
        lastCommand = True
        
    foundRule = False   
