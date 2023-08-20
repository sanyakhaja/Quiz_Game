
import random
import string
import tkinter as tk
from tkinter import ttk

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Genie")

        # Create a custom style
        self.style = ttk.Style()
        
        # Configure the style for labels (foreground color, font)
        self.style.configure("TLabel", foreground="purple", font=("Helvetica", 12, "bold"))
        
        # Configure the style for buttons (foreground color, background color, font)
        self.style.configure("TButton", foreground="black", background="grey", font=("Helvetica", 12, "bold"))
        
        # Initialize the GUI components
        self.init_components()

    def init_components(self):
        # Label for password length input
        self.length_label = ttk.Label(self.root, text="Password Length:")
        self.length_label.pack(pady=10)

        # Entry widget to input password length
        self.length_entry = ttk.Entry(self.root)
        self.length_entry.pack()

        # Configure a style for the "Generate Password" button
        self.style.configure("Generate.TButton", background="orange")

        # Button to generate password
        self.generate_button = ttk.Button(self.root, text="Generate Password", style="Generate.TButton", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Configure a style for the password display label
        self.style.configure("PasswordLabel.TLabel", foreground="purple", font=("Arial", 14))

        # Label to display generated password
        self.password_label = ttk.Label(self.root, text="", style="PasswordLabel.TLabel")
        self.password_label.pack()

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                self.password_label.config(text="Invalid length")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(password_length))
            self.password_label.config(text="Generated Password: " + password)
        except ValueError:
            self.password_label.config(text="Invalid length")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
