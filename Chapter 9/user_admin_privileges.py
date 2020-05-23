# Exercises from Chapter 9 of Python Crash Course - Classes


# Exercise 9-7
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


class Admin(User):
    def __init__(self, first_name, last_name, age, height, eye_colour):
        super().__init__(first_name, last_name, age, height, eye_colour)
        self.access = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can edit post", "can delete post",
                           "can add user", "can create superusers"]

    def show_privileges(self):
        if not self.privileges:
            print("You have no privileges")
        else:
            print("You have the following privileges:")
            print(*self.privileges, sep="\n")

"""
# Create an Admin user using the Admin Class
administrator = Admin("Malin", "Kankanamge", 27, 180, "brown")
# Perform a greeting using the method in User
administrator.greet_user()
# Call the show privileges method in the Privileges class
administrator.access.show_privileges()
"""