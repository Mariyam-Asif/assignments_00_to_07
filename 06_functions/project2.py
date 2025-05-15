# Project 2: Count Evens

def get_list_of_ints():
    lst = []
    user_input = input("Enter an integer or press to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")
    return lst

def count_evens(lst):
    count = 0 
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)

def main():
    lst = get_list_of_ints()
    count_evens(lst)

if __name__ == "__main__":
    main()