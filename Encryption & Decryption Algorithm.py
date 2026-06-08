# Decode Labs Project 1: Encryption & Decryption Algorithm
#Author: [Karan]

import string

def encrypt(text, n):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = n % 26
            if char.islower():
                result += chr((ord(char) + shift_amount - ord('a')) % 26 + ord('a'))
            else:
                result += chr((ord(char) + shift_amount - ord('A')) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, n):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = n % 26
            if char.islower():
                result += chr((ord(char) - shift_amount - ord('a')) % 26 + ord('a'))
            else:
                result += chr((ord(char) - shift_amount - ord('A')) % 26 + ord('A'))
        else:
            result += char
    return result


print("\n\n=======Encryption & Decryption Algorithm=======\n\n")
option = int(input("Choose an option:\n1. Encrypt a string\n2. Decrypt a string\nEnter your choice (1 or 2): "))

if(option == 1):
    str1 = input("Enter the string to encrypt: ")
    shift = int(input("Enter the shift value (1-25): "))
    encrypted_str = encrypt(str1, shift)
    print(f"Encrypted string: {encrypted_str}")

elif (option == 2):
    encrypted_str = input("Enter the string to decrypt: ")
    shift = int(input("Enter the shift value (1-25): "))
    decrypted_str = decrypt(encrypted_str, shift)
    print(f"Decrypted string: {decrypted_str}")

else:
    print("Invalid option. Please choose either 1 or 2.")
