# Project 3: In Stock
def num_in_stock(fruit):
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'jackfruit':
        return 1
    if fruit == 'pear':
        return 100
    else:
        return 0

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock == 0:
        print("This fruit is not in stock.")
    else: 
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == "__main__":
    main()