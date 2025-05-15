# Project 0: Count Numbers

# Get Numbers from the User
def get_user_numbers():
    user_numbers = [] 

    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

# Count how many times each number appears
def count_nums(num_list):
    num_dict = {}
    for num in num_list:
        if num not in num_dict:
            num_dict[num] = 1 # If it's not in the dictionary, add it with count 1
        else:
            num_dict[num] += 1 # If it's already there, increase the count by 1
    return num_dict

# Print the result
def print_counts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == "__main__":
    main()