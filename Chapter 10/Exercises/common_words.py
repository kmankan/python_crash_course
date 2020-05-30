# Exercise 10-10 from Chapter 10 - Files and Exceptions


from os import system


def count_a_word():
    while True:
        filename = input(
            "Enter the filename of the text "
            "you want to analyse: ")
        word = input("Enter the word or phrase "
                     "you want to find "
                     "the number of instances of: ")
        try:
            with open(filename) as f:
                text = f.read().lower()
                word_count = text.count(word)
                print(f"The word '{word}' appears {word_count} "
                      f"times in {filename}.")

        except FileNotFoundError:
            print(f"I couldn't find a file named {filename} in this directory")
            print('\n')
            continue

        else:
            while True:
                question = input("\nContinue (y/n)? ").lower()
                if question == 'y':
                    break
                elif question == 'n':
                    return
                else:
                    continue


count_a_word()
