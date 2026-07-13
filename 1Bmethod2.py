import math

def encrypt(text, key):
    text = text.replace(" ", "")
    rows = math.ceil(len(text) / key)

    matrix = [['' for _ in range(key)] for _ in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(key):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1
            else:
                matrix[i][j] = 'X'

    cipher = ""
    for j in range(key):
        for i in range(rows):
            cipher += matrix[i][j]

    return cipher


def decrypt(cipher, key):
    rows = math.ceil(len(cipher) / key)

    matrix = [['' for _ in range(key)] for _ in range(rows)]

    index = 0
    for j in range(key):
        for i in range(rows):
            if index < len(cipher):
                matrix[i][j] = cipher[index]
                index += 1

    text = ""
    for i in range(rows):
        for j in range(key):
            text += matrix[i][j]

    return text.rstrip('X')


message = input("Enter Message: ")
key = int(input("Enter Number of Columns: "))

encrypted = encrypt(message, key)
print("Encrypted Message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Message:", decrypted)