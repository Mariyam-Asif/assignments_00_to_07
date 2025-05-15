# Project 5: Is Odd

def is_odd(value: int):
    return value % 2 == 1

def main():
    for i in range(10, 20):
        if is_odd(i):
            print(i, "odd")
        else:
            print(i, "even")

if __name__ == "__main__":
    main()