# Exercises from Chapter 9 of Python Crash Course - Classes


from user import User
from privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, age, height, eye_colour):
        super().__init__(first_name, last_name, age, height, eye_colour)
        self.access = Privileges()
