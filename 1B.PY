def encrypt(text, key):
    rail = ['' for _ in range(key)]
    row = 0
    direction = 1

    for char in text:
        rail[row] += char
        row += direction

        if row == key - 1 or row == 0:
            direction *= -1

    return ''.join(rail)


def decrypt(cipher, key):
    n = len(cipher)

    # Create pattern
    pattern = [['' for _ in range(n)] for _ in range(key)]

    row = 0
    direction = 1

    for col in range(n):
        pattern[row][col] = '*'
        row += direction

        if row == key - 1 or row == 0:
            direction *= -1

    index = 0
    for i in range(key):
        for j in range(n):
            if pattern[i][j] == '*' and index < n:
                pattern[i][j] = cipher[index]
                index += 1

    result = ""
    row = 0
    direction = 1

    for col in range(n):
        result += pattern[row][col]
        row += direction

        if row == key - 1 or row == 0:
            direction *= -1

    return result


# Main Program
message = input("Enter the message: ")
key = int(input("Enter number of rails: "))

encrypted = encrypt(message, key)
print("Encrypted Message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Message:", decrypted)