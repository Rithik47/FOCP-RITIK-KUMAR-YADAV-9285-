''' Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2). '''

def int_to_binary():
    n = int(input("Enter a positive integer: "))
    binary = "" # Empty string to represent in binary
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Test the function
print("The equivalent binary of the integer is", int_to_binary())  # Asks for input and prints the binary representation