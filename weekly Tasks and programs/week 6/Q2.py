''' Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original). '''

def find_factors():
    n = int(input("Enter a positive integer: "))
    print("The factors of %d are:" % n, end=" ") # end = "" leaves a space printing in the same line
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()
find_factors()