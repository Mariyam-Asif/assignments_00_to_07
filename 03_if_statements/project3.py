# Project 3: Leap Year
"""
A year is a leap year if:

It is divisible by 4, and...

Not divisible by 100, unless...

It is divisible by 400 (then it is a leap year again!)

"""
def main():
    year = int(input('Please input a year:  '))
    # Check if year is divisible by 4
    if year % 4 == 0:
        # Check if it is divisible by 100
        if year % 100 == 0:
            # Check if it is divisible by 400
            if year % 400 == 0:
                print("That's a leap year!")
            else: 
                print("That's not a leap year!")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year!")

if __name__ == "__main__":
    main()