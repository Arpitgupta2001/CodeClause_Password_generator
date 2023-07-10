import string
import random
import tkinter as tk

def generate_password():
    password_length = length_entry.get()
    password_length = int(password_length)
    if password_length < 8:
        result_label.config(text="Password length must be at least 8 characters.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        result_label.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")

# Create and pack the widgets
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the main loop
window.mainloop()
