# Project 1: Chaotic Counting

import random

DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    for i in range(10):
        curr_value = i + 1
        if done():
            return True
        print(curr_value)

def done():
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()