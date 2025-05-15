# Project 1: Fibonacci Number

MAX_TERm_VALUE: int = 10000 # Set the maximum value for Fibonacci terms

def main():
    curr_term = 0
    next_term = 1
    while curr_term <= MAX_TERm_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term # curr_term becomes what next_term was
        next_term = term_after_next #  next_term becomes the new number

if __name__ == "__main__":
    main()