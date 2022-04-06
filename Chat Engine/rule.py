class rule:
    def __init__(self, uLevel, userInput, robotOutput):
        self.uLevel = uLevel
        self.userInput = userInput
        self.robotOutput = robotOutput
        self.children = []

    def print(self):
        print(self.type + " " + self.input + " ")
        for item in self.output:
            print(item)

    def getLastChild(self):
        return self.children[len(self.children)-1]

    def addChild(self, child):
        self.children.append(child)

    def printFullArray(self, x):
        print('Array Index ' + str(self.uLevel))
        print(self.userInput)
        for y in range (0, len(self.children)):
            self.children[y].printFullArray(y)