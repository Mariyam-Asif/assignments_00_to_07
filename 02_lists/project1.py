# Project 1: Add a list of numbers

def add_many_numbers(numbers) -> int:
    """ Takes in a list of numbers and returns the sum of those numbers. """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    # List of numbers
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Call the function snd store the result
    sum_of_numbers: int = add_many_numbers(numbers)
    # Print the sum
    print(sum_of_numbers)

if __name__ == '__main__':
    main()