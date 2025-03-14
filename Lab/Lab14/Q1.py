import time

class TrafficLight:
    def __init__(self):
        self.color = "red"
        self.duration = 4

    def setTimer(self, t):
        self.duration = t

    def changeColor(self):
        if self.color == "red":
            self.color = "green"
            self.setTimer(3)

        elif self.color == "green":
            self.color = "yellow"
            self.setTimer(2)
            
        else:
            self.color = "red"
            self.setTimer(4)
            
    def tick(self):
        for i in range(self.duration):
            print(self.duration)
            self.duration -= 1

    def start(self):
        print("Traffic Light is starting")
        while True:
            print(f"Color changed to {self.color}")
            self.tick()
            self.changeColor()

T = TrafficLight()
T.start()