
class Alarm_Clock:
    def __init__(self, curTime, onOrOff, setTime):
        self.cutTime = curTime
        self.onOrOff = onOrOff
        self.setTime = setTime

    #Method to set the current time 
    def setCurTime(self,inputTime):
        self.cutTime = inputTime
        print("The current time is " + self.cutTime)

    #Turn on or off alarm
    def switchAlarmOnOff(self):
        if (self.onOrOff == False):
            self.onOrOff = True
        else:
            self.onOrOff = False
        print(self.onOrOff)

    #Set alarm time
    def setAlarmTime(self,inputTime):
        self.setTime = inputTime
        print("The current alarm is set to " + self.setTime) 