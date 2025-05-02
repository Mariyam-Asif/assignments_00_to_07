# Project 3: Feet to inches

INCHES_IN_FOOT: int = 12

def main():
    # Take input from user to enter the number of feet and inches separately
    feet = float(input("Enter number of feet: "))
    extra_inches = float(input("Enter number of extra inches: "))

    # Convert total to inches
    total_inches = (feet * INCHES_IN_FOOT) + extra_inches

    print(f"{feet} feet {extra_inches} inches is equal to {total_inches} inches!")

if __name__ == '__main__':
    main()
