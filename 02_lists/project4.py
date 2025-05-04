# Project 4: Add three copies

def add_three_copies(mylist, data):
    for i in range(3):
        mylist.append(data)

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before: ", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()