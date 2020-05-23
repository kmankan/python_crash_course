# Exercises from Chapter 9 of Python Crash Course - Classes


class User:
    """Model information about a typical user"""

    def __init__(self, first_name, last_name, age, height, eye_colour):
        """Initialise user information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.eye_colour = eye_colour
        self.login_attempts = 0

    def describe_user(self):
        """Create a full description of the users attributes"""
        print(f"The user has the following attributes:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}cm")
        print(f"Eye Colour: {self.eye_colour}")

    def greet_user(self):
        """Create a greeting for the user"""
        print(f"\nHey {self.first_name} {self.last_name}, great to finally"
              f" meet you.\n\n")

    def increment_login_attempts(self):
        """Count incrementally the number of attempted logins"""
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        """"Reset the count of login attempts to zero"""
        self.login_attempts = 0
        print(f"Login attempts: {self.login_attempts}")
