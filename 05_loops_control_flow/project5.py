# Project 5: Double It

def main():
    curr_value = int(input("Enter a number to start doubling: "))

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == "__main__":
    main()