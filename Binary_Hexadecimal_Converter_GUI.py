import tkinter as tk
from tkinter import messagebox

# Convert to binary
def Convert_2_Bin(input_num):
    binary_num = ''
    if input_num == 0:
        binary_num = '0'
    while input_num >= 1:
        # Digits of binary_num are the remainders of the division of 2
        binary_num = str(input_num % 2) + binary_num
        input_num = input_num // 2
    return binary_num

# Convert to hexadecimal
def Convert_2_Hex(input_num):
    # Define hex digits
    hex_digits = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    hex_num = ''
    if input_num == 0:
        hex_num = '0'
    while input_num >= 1:
        # Digits of binary_num are the remainders of the division of 16
        hex_num = hex_digits[input_num % 16] + hex_num
        input_num = input_num // 16
    return hex_num

# Action of Convert Buttom
def Convert():
    # Get the decimal number from the entry widget
    try:
        decimal_num = int(entry.get())
        if not 0 <= decimal_num <= 255:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid integer between 0 and 255.")
        return

    # Convert to binary and hexadecimal
    binary_num = Convert_2_Bin(decimal_num)
    hex_num= Convert_2_Hex(decimal_num)

    # Update the labels with the results
    binary_label.config(text="Binary representation: " + binary_num)
    hex_label.config(text="Hexadecimal representation: " + hex_num)

# Create the main window
window = tk.Tk()
window.title("Binary and Hexadecimal Converter")

# Get the screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the size and position of the window
width = 400
height = 150
x = (screen_width - width) // 2
y = (screen_height - height) // 2
window.geometry(f"{width}x{height}+{x}+{y}")

# Add a label to prompt the user to enter a decimal number
decimal_label = tk.Label(window, text="Enter a decimal number:")
decimal_label.pack()

# Add an entry widget to allow the user to enter a decimal number
entry = tk.Entry(window)
entry.pack()

# Add a button to trigger the conversion
button = tk.Button(window, text="Convert", command=Convert)
button.pack()

# Add labels to display the binary and hexadecimal representations
binary_label = tk.Label(window, text="Binary representation:")
binary_label.pack()
hex_label = tk.Label(window, text="Hexadecimal representation:")
hex_label.pack()

# Start the GUI event loop
window.mainloop()