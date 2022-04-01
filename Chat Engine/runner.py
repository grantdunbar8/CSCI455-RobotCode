from rule import *

file = open('testing1.txt', 'r')

lines = file.readlines()

rules = []
type=''
childCount = 0
for line in lines:
    

    if '#' not in line[0]:
        # if len(type) > 0 and type.split('u')[1] < line.split(':')[0].replace(' ', '').split('u')[1]:
        #     #print("TYPE: " + type.split('u')[1] + " | LINE: " + line.split(':')[0].replace(' ', '').split('u')[1])
        #     print('CHILD')
            
        # elif len(type) > 0 and type.split('u')[1] > line.split(':')[0].replace(' ', '').split('u')[1] and len(line.split(':')[0].replace(' ', '').split('u')[0]) is not NULL: 
        #     print("LINE2: " + line.split(':')[0].replace(' ', '').split('u')[0] + ":")
        #     print("CHILD")
        type = line.split(':')[0].replace(' ', '')
        if(type == 'u'):
            print("LINE: " + line)

            
            input = line.split(':')[1].split('(')[1].split(')')[0]
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
                    isQuote = False
                    strBuilder = ''
                    for element in range(0, len(outputLine)):
                        print(outputLine[element])
                        if outputLine[element] != ' ' and outputLine[element] != '\"' and isQuote == False:
                            strBuilder += outputLine[element]
                        elif outputLine[element] == ' ' and isQuote == False and len(strBuilder) > 0:
                            output.append(strBuilder)
                            print("BUILD :  " + strBuilder)
                            strBuilder = ''
                        elif outputLine[element] == '\"' and isQuote == False:
                            isQuote = True
                        elif outputLine[element] == '\"' and isQuote == True:
                            output.append(strBuilder)
                            strBuilder = ''
                            isQuote = False
                        elif outputLine[element] != '\"' and isQuote == True:
                            strBuilder += outputLine[element]
                    output.append(strBuilder)
                rules.append(rule(type, input, output))
            else:
                print('ERROR in this line')
        else:
            if len(line.split(':')) > 2:
                childCount = int(type.split('u')[1])
                output = 'lit'
                childOfRule = rules[len(rules)-1]
                for x in range (1, childCount):
                    childOfRule = childOfRule.getLastChild()
                
                childOfRule.addChild(rule(type, input, output))
            else:
               print('ERROR in this line') 
        
        
for item in rules:
    item.print()
    item.printChildren() 

file.close()