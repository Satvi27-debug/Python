import tkinter as tk

# Function for the submit action
def submit_action():
    print("Submitted:", entry1.get(), entry2.get())

# Function for the reset action
def reset_action():
    entry1.delete(0, tk.END)  # Clear the text of entry1
    entry2.delete(0, tk.END)  # Clear the text of entry2

# Create main window
root = tk.Tk()
root.title("Window Wizard")
root.geometry("300x200")

# Create labels
label1 = tk.Label(root, text="Label 1:")
label1.pack(pady=5)
label2 = tk.Label(root, text="Label 2:")
label2.pack(pady=5)

# Create text fields (Entry widgets)
entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Create buttons
submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_action)
reset_button.pack(pady=5)

# Run the GUI
root.mainloop()