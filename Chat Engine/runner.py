from rule import *

file = open('testing1.txt', 'r')

lines = file.readlines()

rules = []
numLines = len(lines)

lSplit = []
uLevel = 0
userInput = ""
robotOutput = ""

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
                parsedInput.append(lSplit[1].split("\""))
            else:
                parsedInput.append(lSplit[1])
            print("PARSED INPUT")
            print(parsedInput)
            print("\n")

        # Handle robot output
        if "[" not in lSplit[2]:
            parsedOutput = []
            if "\"" in lSplit[2]:
                parsedOutput.append(lSplit[2].split("\""))
            else:
                parsedOutput.append(lSplit[2])
            print("PARSED OUTPUT")
            print(parsedOutput)
            print("\n")

        if uLevel == 0:
            # If the uLevel is equal to 0
            print("uLevel was 0")
            print(uLevel)
        else:
            # If the uLevel us not equal to 0
            print("uLevel was NOT 0")
            print(uLevel)
    else:
        # Here if line was a comment
        print("^ Line is a comment\n\n")

        
##        if len(type) > 0 and type.split('u')[1] < line.split(':')[0].replace(' ', '').split('u')[1]:
##            print('CHILD')
##        type = line.split(':')[0].replace(' ', '')
##        input = line.split(':')[1].split('(')[1].split(')')[0]
##        print(len(input))
##        if len(line.split(':')) > 2:
##            output = []
##            if '[' not in line.split(':')[2]:
##                if '\"' in line.split(':')[2]:
##                    output.append(line.split(':')[2].split('\"')[1])
##                else:
##                    output.append(line.split(':')[2])
##            else:
##                outputLine = line.split(':')[2].split('[')[1].split(']')[0]
##                print("LINE HERE: " + outputLine)
##                isQuote = FALSE
##                strBuilder = ''
##                for element in range(0, len(outputLine)):
##                    print(outputLine[element])
##                    if outputLine[element] != ' ' and outputLine[element] != '\"' and isQuote == FALSE:
##                        strBuilder += outputLine[element]
##                    elif outputLine[element] == ' ' and isQuote == FALSE and len(strBuilder) > 0:
##                        output.append(strBuilder)
##                        print("BUILD :  " + strBuilder)
##                        strBuilder = ''
##                    elif outputLine[element] == '\"' and isQuote == FALSE:
##                        isQuote = TRUE
##                    elif outputLine[element] == '\"' and isQuote == TRUE:
##                        output.append(strBuilder)
##                        strBuilder = ''
##                        isQuote = FALSE
##                    elif outputLine[element] != '\"' and isQuote == TRUE:
##                        strBuilder += outputLine[element]
##                output.append(strBuilder)
##            rules.append(rule(type, input, output, 'lit'))
##        else:
##            print('ERROR in this line')
##        
##        
##for item in rules:
##    item.print()

file.close()
