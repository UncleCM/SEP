class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def set(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def get(self):
        return self.hours, self.minutes, self.seconds
    
    def printTime(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} Hrs.")


time1 = Time(9, 30, 0)
time1.printTime()