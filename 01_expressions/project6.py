# Project 6: Roll dice

import random

NUM_OF_SIDES = 6

def main():
    random.seed(1) # Ensures the dice rolls are the same every time the program runs

    die1 = random.randint(1, NUM_OF_SIDES)
    die2 = random.randint(1, NUM_OF_SIDES)
    total = die1 + die2

    print("Dice have", NUM_OF_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die: ", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()