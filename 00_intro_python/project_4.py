# Project 4: Age Riddle Solver

def main():

    # Storing ages based on given conditions
    anton = 21
    beth = anton + 6 # Beth is 6 years older than Anton
    chen = beth + 20 # Chen is 20 years older than Beth
    drew = chen + anton # Drew is as old as Chen's age + Anton's age
    ethan = chen # Ethan is the same age as Chen

    # Printing the ages
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

if __name__ == '__main__':
    main()