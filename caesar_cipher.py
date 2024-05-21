def caesar_encrypt(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(message, shift):
    return caesar_encrypt(message, -shift)

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (0-25): "))
    if 0 <= shift <= 25:
        encrypted = caesar_encrypt(message, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)
    else:
        print("Shift value must be between 0 and 25.")

if __name__ == "__main__":
    main()
