
class Alarm_Clock:
    def __init__(self):
        self.alarm_set = False

    def switchAlarmOnOff(self):
        if (self.alarm_set == False):
            self.alarm_set = True
        else: 
            self.alarm_set = False

    