# Project 5: Calculate the perimeter of a triangle

def main():
    # Take user input
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the sum of the sides
    perimeter = side1 + side2 + side3

    # Print the result with two decimal places for better readability
    print(f"The perimeter of the triangle is {perimeter:.2f}")

if __name__ == '__main__':
    main()