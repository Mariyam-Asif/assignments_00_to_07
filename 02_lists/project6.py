# Project 6: Get last element of list

def get_last_element(lst):
    ## print(lst[len(lst)-1])
    print(lst[-1]) ## shorter way

def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == "__main__":
    main()