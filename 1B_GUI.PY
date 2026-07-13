from tkinter import *
from tkinter import messagebox

# Encryption Function
def encrypt():
    text = message_entry.get()

    try:
        key = int(key_entry.get())
        if key < 2:
            messagebox.showerror("Error", "Key must be at least 2.")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid key.")
        return

    rail = ['' for _ in range(key)]
    row = 0
    direction = 1

    for char in text:
        rail[row] += char
        row += direction

        if row == key - 1 or row == 0:
            direction *= -1

    result = ''.join(rail)

    output.delete(0, END)
    output.insert(0, result)


# Decryption Function
def decrypt():
    cipher = message_entry.get()

    try:
        key = int(key_entry.get())
        if key < 2:
            messagebox.showerror("Error", "Key must be at least 2.")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid key.")
        return

    n = len(cipher)

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

    output.delete(0, END)
    output.insert(0, result)


# Clear Function
def clear():
    message_entry.delete(0, END)
    key_entry.delete(0, END)
    output.delete(0, END)


# GUI Window
root = Tk()
root.title("Rail Fence Cipher")
root.geometry("450x320")
root.resizable(False, False)

Label(root, text="Rail Fence Cipher", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Enter Message").pack()
message_entry = Entry(root, width=40)
message_entry.pack(pady=5)

Label(root, text="Enter Number of Rails (Key)").pack()
key_entry = Entry(root, width=10)
key_entry.pack(pady=5)

Button(root, text="Encrypt", width=15, command=encrypt).pack(pady=5)

Button(root, text="Decrypt", width=15, command=decrypt).pack(pady=5)

Button(root, text="Clear", width=15, command=clear).pack(pady=5)

Label(root, text="Result").pack()

output = Entry(root, width=40)
output.pack(pady=5)

root.mainloop()