
class Alarm_Clock:
    def __init__(self, curTime, onOrOff, setTime):
        self.cutTime = curTime
        self.onOrOff = onOrOff
        self.setTime = setTime

    #Method to set the current time 
    def setCurTime(self,inputTime):
        self.cutTime = inputTime
        print(self.cutTime)

    def switchAlarmOnOff(self):
        if (self.alarm_set == False):
            self.alarm_set = True
        else: 
            self.alarm_set = False

    