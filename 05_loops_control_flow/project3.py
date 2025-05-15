# Project 3: Wholesome Machine

AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    user_feedback = input() # Get user input

    while user_feedback != AFFIRMATION: # Repeat until it's exactly right
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()
    
    print("That's right! :)")

if __name__ == "__main__":
    main()