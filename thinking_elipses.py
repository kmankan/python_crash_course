# A module that adds a timed elipses that mimics thinking effect

from time import sleep


class Thinking:
    "Model the act of thinking using ellipses"
    # dots is the number of ellipses and time the time between each showing
    def __init__(self, dots, time):
        self.dots = dots
        for i in range(self.dots):
            print(".", end="")
            sleep(time)

