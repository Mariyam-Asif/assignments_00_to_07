# Project 8: Tiny Mad Lib

# Constant part of the sentence
START_SENTENCE: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # Take input from user for an adjective, noun and a verb
    adjective: str = input("Please enter an adjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please enter a verb and press enter: ")
    
    print(START_SENTENCE + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()