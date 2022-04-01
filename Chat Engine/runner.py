from pickle import FALSE, TRUE
from rule import *

file = open('testing1.txt', 'r')

lines = file.readlines()

rules = []
type=''
for line in lines:
    print("LINE: " + line)
    

    if '#' not in line[0]:
        if len(type) > 0 and type.split('u')[1] < line.split(':')[0].replace(' ', '').split('u')[1]:
            print('CHILD')
        type = line.split(':')[0].replace(' ', '')
        input = line.split(':')[1].split('(')[1].split(')')[0]
        print(len(input))
        if len(line.split(':')) > 2:
            output = []
            if '[' not in line.split(':')[2]:
                if '\"' in line.split(':')[2]:
                    output.append(line.split(':')[2].split('\"')[1])
                else:
                    output.append(line.split(':')[2])
            else:
                outputLine = line.split(':')[2].split('[')[1].split(']')[0]
                print("LINE HERE: " + outputLine)
                isQuote = FALSE
                strBuilder = ''
                for element in range(0, len(outputLine)):
                    print(outputLine[element])
                    if outputLine[element] != ' ' and outputLine[element] != '\"' and isQuote == FALSE:
                        strBuilder += outputLine[element]
                    elif outputLine[element] == ' ' and isQuote == FALSE and len(strBuilder) > 0:
                        output.append(strBuilder)
                        print("BUILD :  " + strBuilder)
                        strBuilder = ''
                    elif outputLine[element] == '\"' and isQuote == FALSE:
                        isQuote = TRUE
                    elif outputLine[element] == '\"' and isQuote == TRUE:
                        output.append(strBuilder)
                        strBuilder = ''
                        isQuote = FALSE
                    elif outputLine[element] != '\"' and isQuote == TRUE:
                        strBuilder += outputLine[element]
                output.append(strBuilder)
            rules.append(rule(type, input, output, 'lit'))
        else:
            print('ERROR in this line')
        
        
for item in rules:
    item.print()

file.close()