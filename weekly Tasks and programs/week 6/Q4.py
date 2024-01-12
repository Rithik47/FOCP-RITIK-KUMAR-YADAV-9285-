'''  Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way. '''

def encrypt_message():
    message = input("Enter a message: ")
    encrypted_message = message.replace(" ", "")[::-1]
    print("The encrypted message is: %s" % encrypted_message)

encrypt_message()