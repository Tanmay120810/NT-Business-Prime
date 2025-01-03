import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Functions
def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - PARASHAR Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{file_path} - PARASHAR Notepad")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Save File", "File saved successfully!")
    else:
        save_as_file()

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - PARASHAR Notepad")
        messagebox.showinfo("Save File", "File saved successfully!")

# Initialize the app
root = tk.Tk()
root.title("PARASHAR Notepad")
root.geometry("800x600")

# Global variable for current file
current_file = None

# UI Enhancements
# Text Area
text_area = tk.Text(root, wrap="word", undo=True, font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Menu
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as_file, accelerator="Ctrl+shift+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q")
menu_bar.add_cascade(label="File", menu=file_menu)

# Add the menu to the main window
root.config(menu=menu_bar)

# Status Bar
status_bar = tk.Label(root, text="Ready", anchor="w", relief="sunken", bg="lightgray")
status_bar.pack(side="bottom", fill="x")

# Key Bindings
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-q>", lambda event: root.quit())

# Run the application
root.mainloop()

#End Of The Project
