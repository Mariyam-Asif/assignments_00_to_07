# Program 1: Dice Simulator

import random # random module to generate random numbers

# define how many sides the dice have
NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES) # First dice roll
    die2 = random.randint(1, NUM_SIDES) # Second dice roll
    total = die1 + die2 
    print("Total of two dice:", total)

def main():
    # This shows variable scope by using die1 here too.
    die1 = 10 # Local to main()
    print("die in main() starts as:", die1)

    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() is:", die1) # Shows that die1 in main() hasn't changed

if __name__ == '__main__':
    main()