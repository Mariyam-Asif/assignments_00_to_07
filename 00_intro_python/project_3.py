# Project 3: Fahrenheit to Celsius

def main():
    # Take temperature from user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Converts Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print(f"Temperature: {fahrenheit:.1f}F = {celsius:.6f}C")

if __name__ == '__main__':
    main()