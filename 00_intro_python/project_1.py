# Program 1 : Add two numbers

def main():
    print("Welcome! This program calculates the sum of two numbers.")

    # Get the first number from the user
    num1 = int(input("Enter the first number: "))

    # Get the second number from the user
    num2 = int(input("Enter the second number: "))

    # Calculate the sum
    total = num1 + num2

    print(f"The total is {total}.")

if __name__ == '__main__':
    main()