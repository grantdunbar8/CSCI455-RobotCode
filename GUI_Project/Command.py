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
        exeAngle = inDegrees

    def ExecuteCommand():
        # exeType can be integers or strings or any type of variable
        # whatever works best.
        if exeType == 1:
            print("TYPE: move forward")
        elif exeType == 2:
            print("TYPE: move back")
        elif exeType == 3:
            print("TYPE: turn right")
        elif exeType == 4:
            print("TYPE: turn left")
        elif exeType == 5:
            print("TYPE: head up")
        elif exeType == 6:
            print("TYPE: head down")
        elif exeType == 7:
            print("TYPE: head left")
        elif exeType == 8:
            print("TYPE: head right")
        elif exeType == 9:
            print("TYPE: rotate right")
        elif exeType == 10:
            print("TYPE: rotate left")
