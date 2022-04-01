class rule:
    def __init__(self, type, input, output, children):
        self.type = type
        self.input = input
        self.output = output
        self.children = children

    def print(self):
        print(self.type + " " + self.input + " ")
        for item in self.output:
            print(item)