class rule:
    def __init__(self, uLevel, userInput, robotOutput, children):
        self.uLevel = uLevel
        self.userInput = userInput
        self.robotOutput = robotOutput
        self.children = children

    def print(self):
        print(self.type + " " + self.input + " ")
        for item in self.output:
            print(item)
