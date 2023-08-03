import tkinter as tk
from tkinter import filedialog

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        elif char.isspace():
            encrypted_text += ' '
        else:
            encrypted_text += encrypted_char
    return encrypted_text

def encrypt_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
        encrypted_text = caesar_cipher(text, 3) # using a shift of 3 right
        save_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if save_file_path:
            with open(save_file_path, 'w') as file:
                file.write(encrypted_text)
                print("File encrypted and saved successfully.")

root = tk.Tk()
root.title("Caesar Cipher Encryption")

upload_button = tk.Button(root, text="Upload File", command=encrypt_file)
upload_button.pack(pady=20)

root.mainloop()