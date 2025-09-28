

# TASK_1
'''CREATE A PROGRAM THAT CAN ENCRYPT AND DECRYPT TEXT USING THE CAESAR CIPHER ALGORITHM. 
ALLOW USERS TO INPUT A MESSAGE AND A SHIFT VALUE TO PERFORM ENCRYPTION AND DECRYPTION.
'''
def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isupper():  
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():  
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:  
            result += char
    return result

def decrypt(message, shift):
    result = ""
    for char in message:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    return result

message = input("Enter a message: ")
shift = int(input("Shift the value:"))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\nEncrypted Message:", encrypted)
print("Decrypted Message:", decrypted)


