# Exercise 10-1 in Chapter 10 - Files and Exceptions

filename = "learning_python.txt"


def learn_python():
    with open(filename) as file_object:
        contents = file_object.read()
        print(contents + "\n")

    with open(filename) as file_object:
        for sentence in file_object:
            print(sentence.rstrip())
        print("\n")

    with open(filename) as file_object:
        lines = file_object.readlines()

    learn_string = ''
    for line in lines:
        learn_string += line
    print(learn_string)
    print("\n* * *\n")


def replace_python_with_x(x):
    """A function that repeats the read action above but replaces the word
    'Python' from the text file with a user selected programming language
    (e.g. 'C')."""
    with open(filename) as file_object:
        lines = file_object.readlines()

    text_strings = ''
    for line in lines:
        text_strings += line.replace('Python', x)
    print(text_strings)


learn_python()
replace_python_with_x('C')
