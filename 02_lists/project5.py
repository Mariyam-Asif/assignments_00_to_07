# Project 5: Get first element

def get_first_elemenet(lst):
    print(lst[0])

def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_elemenet(lst)

if __name__ == "__main__":
    main()