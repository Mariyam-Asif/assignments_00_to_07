# Project 5: Remainder Division

def main():
    try:
        # Get the numbers from user
        dividend: int = int(input("Please enter an integer to be divided: "))
        divisor: int = int(input("Please enter an integer to divide by: "))

        # Check for divide by zero error
        if divisor == 0:
            print("Not possible to divide by 0. Please re-run the program with a non-zero divisor.")
            return
        
        # Calculate the quotient and remainder
        quotient: int = dividend // divisor
        remainder: int = dividend % divisor

        print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

    except ValueError:
        print("Invalid input! Please enter whole numbers only.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

if __name__ == '__main__':
    main()