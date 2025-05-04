# Project 4: Tall Enough to Ride

MINIMUN_HEIGHT:int = 50
def main():
    while True:
        user_input = input("How tall are you in inches? (Press enter to quit.)")
        if user_input == "":
            break

        height = float(user_input)
        if height >= MINIMUN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride!")
        
if __name__ == "__main__":
    main()