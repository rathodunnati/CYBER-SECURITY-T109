from tkinter import *
from tkinter import messagebox

# Encryption Function
def encrypt():
    text = message_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid shift key!")
        return

    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    output.delete(0, END)
    output.insert(0, result)


# Decryption Function
def decrypt():
    text = message_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid shift key!")
        return

    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char

    output.delete(0, END)
    output.insert(0, result)


# Clear Function
def clear():
    message_entry.delete(0, END)
    shift_entry.delete(0, END)
    output.delete(0, END)


# GUI Window
root = Tk()
root.title("Encryption & Decryption")
root.geometry("450x300")
root.resizable(False, False)

Label(root, text="Encryption & Decryption", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Enter Message").pack()
message_entry = Entry(root, width=40)
message_entry.pack(pady=5)

Label(root, text="Enter Shift Key").pack()
shift_entry = Entry(root, width=10)
shift_entry.pack(pady=5)

Button(root, text="Encrypt", width=12, command=encrypt).pack(pady=5)

Button(root, text="Decrypt", width=12, command=decrypt).pack(pady=5)

Button(root, text="Clear", width=12, command=clear).pack(pady=5)

Label(root, text="Result").pack()

output = Entry(root, width=40)
output.pack(pady=5)

root.mainloop()