import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        
        self.length_label = ttk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.length_entry = ttk.Entry(master, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)
        self.length_entry.insert(0, "12")
        
        self.complexity_label = ttk.Label(master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.complexity_combobox = ttk.Combobox(master, values=["Low", "Medium", "High"], width=10)
        self.complexity_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.complexity_combobox.current(1)
        
        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)
        
        self.password_label = ttk.Label(master, text="Generated Password:")
        self.password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
        
        self.password_entry = ttk.Entry(master, width=30, state="readonly")
        self.password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        
        self.copy_button = ttk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)
        
    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_combobox.get()
        
        if complexity == "Low":
            chars = string.ascii_letters + string.digits
        elif complexity == "Medium":
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
        
        try:
            password = ''.join(random.choice(chars) for _ in range(length))
            self.password_entry.config(state="normal")
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            self.password_entry.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Invalid password length.")
            
    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard.")
        else:
            messagebox.showwarning("Warning", "No password generated yet.")
        

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()