# Exercises from Chapter 9 of Python Crash Course - Classes

from random import randint, choice
from time import sleep

class Die:
    """A class that represents an n-sided die and rolls of that die"""
    def __init__(self, sides=6):
        """Initialise the die and how many faces it has"""
        self.sides = sides

    def roll_die(self, rolls):
        """A method that rolls the built dice n-times"""
        print(f"Rolling a {self.sides}-sided die {rolls} times...")
        sleep(0.5)
        # Roll the dice 'rolls' number of times
        for i in range(rolls):
            # If statement to ensure the last roll doesn't print a comma
            if i == rolls-1:
                print(randint(1, self.sides))
            # Print all dice rolls on same line separated by a comma
            else:
                print(randint(1, self.sides), end=",")
            # Add a short break between rolls for dramatic effect
            sleep(0.5)
        print("\n")


six_die = Die(6)
six_die.roll_die(10)

ten_die = Die(10)
ten_die.roll_die(10)

twenty_die = Die(20)
twenty_die.roll_die(10)




