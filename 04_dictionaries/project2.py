# Project 2: Phonebook 

def read_phone_numbers():
    phonebook = {}

    while True: 
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name.lower()] = number
    return phonebook

def print_phonebook(phonebook):
    print("\nPhonebook entries:")
    for name in phonebook:
        print(str(name) + "->" + str(phonebook[name]))

def lookup_numbers(phonebook):
    print("\nLookup Numbers:")
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        key = name.lower()
        if key not in phonebook:
            print(name + "is not in the phonebook.")
        else:
            print(name + "'s number is: " + phonebook[key])

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == "__main__":
    main()