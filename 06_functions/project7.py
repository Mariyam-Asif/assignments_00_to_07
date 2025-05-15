# Project 7: Print Multiple

def print_multiple(message: str, repeat: int):
    for i in range(repeat):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()