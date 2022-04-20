class Command:
    exeDuration = 0
    exeType = 0
    exeAngle = 0
    
    def __init__(self, inTime, inType, inAngle):
        # Duration the movement will be executed
        exeTime = inTime
        
        # Type of motion that will be executed
        exeType = inType
        
        # Angle for rotation or movement
        exeAngle = inAngle

    def ExecuteCommand(self):
        # exeType can be integers or strings or any type of variable
        # whatever works best.
        if self.exeType == 1:
            print("TYPE: move forward")
        elif self.exeType == 2:
            print("TYPE: move back")
        elif self.exeType == 3:
            print("TYPE: turn right")
        elif self.exeType == 4:
            print("TYPE: turn left")
        elif self.exeType == 5:
            print("TYPE: head up")
        elif self.exeType == 6:
            print("TYPE: head down")
        elif self.exeType == 7:
            print("TYPE: head left")
        elif self.exeType == 8:
            print("TYPE: head right")
        elif self.exeType == 9:
            print("TYPE: rotate right")
        elif self.exeType == 10:
            print("TYPE: rotate left")
