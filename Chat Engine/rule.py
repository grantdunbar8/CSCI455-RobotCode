class rule:
    def __init__(self, type, input, output):
        self.type = type
        self.input = input
        self.output = output
        self.children = []

    def print(self):
        print(self.type + " " + self.input + " ")
        for item in self.output:
            print(item)
    
    def getLastChild(self):
        return self.children[len(self.children)-1]

    def addChild(self, rule):
        self.children.append(rule)

    def printChildren(self):
        for child in self.children:
            print("Children: " + child.type)
            child.printChildren()