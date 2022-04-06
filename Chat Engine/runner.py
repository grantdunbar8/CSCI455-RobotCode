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
                parsedInput = lSplit[2].split("\"")
                parsedInput.pop(0)
                parsedInput.pop(len(parsedOutput) - 1)
            else:
                parsedInput.append(lSplit[1])
            print("PARSED INPUT")
            print(parsedInput)
        else:
            # Parses into [thing1, thing2, thingx] form user input
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
            # Parses into [thing1, thing2, thingx] form robot ouotput
            if "\"" in lSplit[2]:
                parsedOutput = lSplit[2].split("[")[1].split("]")[0].split(" ")
                firstQuote = ""
                tempOutput = []
                for i in range(len(parsedOutput)):
                    if "\"" in parsedOutput[i] and firstQuote == "":
                        firstQuote = parsedOutput[i]
                    elif "\"" in parsedOutput[i] and not firstQuote == "":
                        tempString = firstQuote + " " + parsedOutput[i]
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
        else:
            # If the uLevel us not equal to 0
            print("uLevel was NOT 0")
            print(uLevel)
    else:
        # Here if line was a comment
        print("^ Line is a comment\n\n")

file.close()
