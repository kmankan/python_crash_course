# Exercises from Chapter 9 of Python Crash Course - Classes


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
