# Exercises from Chapter 9 of Python Crash Course - Classes

from random import choice,randint,sample
# import the complete list of lowercase ascii characters
from string import ascii_lowercase
from time import sleep
from thinking_elipses import Thinking


"""“
Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list and print a message
saying that any ticket matching these four numbers or letters wins a prize.”
"""


class PlayLottery:
    """Model the structure of a lottery including the composition of
    numbers and letters in the draw pool, and the size of draw (i.e. its
    difficulty). Simulate the drawing of a lottery and running multiple
    lotteries to assess typical probabilities."""
    def __init__(self, numbers, letters, draws):
        """Initialise the lottery"""
        # Generate a list of integers from 0 to 'number'.
        self.numbers = list(range(numbers))
        # Generate a list of lowercase letters, of 'letters' length.
        self.letters = sample(ascii_lowercase,letters)
        # Combine the numbers and letters into one list for a character pool
        self.characters = [*self.numbers, *self.letters]
        # Set the difficulty level of the lottery (i.e. how many ticket items).
        self.lottery_difficulty = draws

    def run_lottery(self):
        """Simulate a lottery where a winning ticket it drawn and then
        count how many tickets need to be randomly generated until
        that winning ticket is replicated."""
        # Tickets are generated as random samples from the character pool,
        # with ticket size equivalent to the difficulty level
        winning_ticket = sample(self.characters, self.lottery_difficulty)
        print(f"Choosing from the following pool: {self.characters}\n"
              f"with a difficulty of {self.lottery_difficulty}")
        sleep(1)
        print(f"\nAnd the winning ticket is", end='')
        # The imported Thinking class adds a thinking ellipse
        Thinking(3, 0.5)
        print("")
        print(winning_ticket)
        print("\nChecking for winners", end='')
        Thinking(5, 0.3)
        sleep(1)

        my_ticket = sample(self.characters, self.lottery_difficulty)
        counter = 0

        # Continue to generate new tickets until a winning-ticket match
        while my_ticket != winning_ticket:
            my_ticket = sample(self.characters, self.lottery_difficulty)
            counter += 1
            print(f"{counter}. {my_ticket}")

        print(f"\nHey entrant {counter}, you won!")

    def run_many(self, iterations):
        """Run numerous cycles of the lottery draw, each time storing how many
        tickets needed to be drawn before a matching ticket was generated.
        Perform some basic statistics (mean, range) on the reported data.
        """
        results = []
        # Run the lottery 'iterations' number of times.
        for i in range(iterations):
            # Define the winning ticket, contestant tickets and a counter
            winning_ticket = sample(self.characters, self.lottery_difficulty)
            my_ticket = sample(self.characters, self.lottery_difficulty)
            counter = 1

            # Continue to generate new tickets until a match is found.
            # Add to counter each time
            while my_ticket != winning_ticket:
                my_ticket = sample(self.characters, self.lottery_difficulty)
                counter += 1

            # At the end of each lottery, add the counter of this draw to the
            # results list.
            results.append(counter)

        print(f"I ran the lottery at Level {self.lottery_difficulty} "
              f"difficulty, "
              f"{iterations} times. Here are the results: \n{results}")
        print(f"\nThe average time was {int(sum(results)/len(results))}")
        print(f"\nThe most time was {results[-1]}")
        print(f"\nThe least time was {results[0]}")


# Create a lottery with (numbers), (letters) and a specific (draw) size.
lottery = PlayLottery(10, 5, 3)
# Run the lottery 'x' number of times
lottery.run_many(10)
