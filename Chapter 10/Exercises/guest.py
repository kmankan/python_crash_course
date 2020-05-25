filename1 = 'guest.txt'
filename2 = 'guest_book.txt'


def guest():
    """Write the name of a single guest into a file"""
    greet = input("Hello, please enter your name: ")
    with open(filename1,'w') as file_object:
        file_object.write(greet)


def guest_book():
    """Run a loop that continuously asks the user to enter names
    into the guest book until the enter the escape character. Append each
    of these names to a text file."""
    while True:
        guest_name = input("Please enter your name for the guest book."
                           " Enter 'q' to quit.\n")
        if guest_name == 'q':
            break
        else:
            print('')

            with open(filename2, 'a') as file_object:
                file_object.write(f"{guest_name}\n")


guest_book()
