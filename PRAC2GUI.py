import tkinter as tk
from tkinter import messagebox
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        e = int(entry_e.get())
        msg = int(entry_msg.get())

        n = p * q
        phi = (p - 1) * (q - 1)

        if gcd(e, phi) != 1:
            messagebox.showerror("Error", "e must be coprime with φ(n).")
            return

        d = mod_inverse(e, phi)

        if d is None:
            messagebox.showerror("Error", "Invalid public exponent.")
            return

        if msg >= n:
            messagebox.showerror("Error", "Message must be less than n.")
            return

        cipher = pow(msg, e, n)
        plain = pow(cipher, d, n)

        lbl_public.config(text=f"Public Key: ({e}, {n})")
        lbl_private.config(text=f"Private Key: ({d}, {n})")
        lbl_cipher.config(text=f"Encrypted Message: {cipher}")
        lbl_plain.config(text=f"Decrypted Message: {plain}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")

root = tk.Tk()
root.title("RSA Encryption and Decryption")
root.geometry("450x450")

tk.Label(root, text="First Prime Number (p)").pack()
entry_p = tk.Entry(root)
entry_p.pack()

tk.Label(root, text="Second Prime Number (q)").pack()
entry_q = tk.Entry(root)
entry_q.pack()

tk.Label(root, text="Public Exponent (e)").pack()
entry_e = tk.Entry(root)
entry_e.pack()

tk.Label(root, text="Message (Integer)").pack()
entry_msg = tk.Entry(root)
entry_msg.pack()

tk.Button(root, text="Encrypt & Decrypt", command=rsa).pack(pady=10)

lbl_public = tk.Label(root, text="")
lbl_public.pack()

lbl_private = tk.Label(root, text="")
lbl_private.pack()

lbl_cipher = tk.Label(root, text="")
lbl_cipher.pack()

lbl_plain = tk.Label(root, text="")
lbl_plain.pack()

root.mainloop()