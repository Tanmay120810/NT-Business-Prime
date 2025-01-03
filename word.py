from tkinter import Tk, Text, Menu, filedialog, messagebox, font, Toplevel, Label, Entry, Button, Scrollbar, RIGHT, Y
import os
from spellchecker import SpellChecker
from reportlab.pdfgen import canvas

class WordApp:
    def __init__(self, master):
        self.master = master
        self.master.title("WordApp - MS Word Like Software")
        self.master.geometry("800x600")
        
        # Text widget for content
        self.text_area = Text(self.master, wrap="word", font=("Arial", 12), undo=True)
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar
        self.scrollbar = Scrollbar(self.text_area, orient="vertical", command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Initialize menu bar
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # File menu
        file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_command(label="Export to PDF", command=self.export_to_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)

        # Edit menu
        edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=lambda: self.text_area.event_generate("<<Undo>>"))
        edit_menu.add_command(label="Redo", command=lambda: self.text_area.event_generate("<<Redo>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        edit_menu.add_command(label="Find and Replace", command=self.find_and_replace)

        # Format menu
        format_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Bold", command=self.make_bold)
        format_menu.add_command(label="Italic", command=self.make_italic)
        format_menu.add_command(label="Underline", command=self.make_underline)
        format_menu.add_separator()
        format_menu.add_command(label="Zoom In", command=self.zoom_in)
        format_menu.add_command(label="Zoom Out", command=self.zoom_out)

        # Tools menu
        tools_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Word Count", command=self.word_count)
        tools_menu.add_command(label="Spell Check", command=self.spell_check)

        # Help menu
        help_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        # Track file name
        self.file_name = None

    def new_file(self):
        self.text_area.delete(1.0, "end")
        self.file_name = None
        self.master.title("Untitled - WordApp")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, "end")
                self.text_area.insert(1.0, content)
                self.file_name = file_path
                self.master.title(f"{os.path.basename(file_path)} - WordApp")

    def save_file(self):
        if self.file_name:
            with open(self.file_name, "w") as file:
                file.write(self.text_area.get(1.0, "end"))
                self.master.title(f"{os.path.basename(self.file_name)} - WordApp")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end"))
                self.file_name = file_path
                self.master.title(f"{os.path.basename(file_path)} - WordApp")

    def export_to_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            pdf = canvas.Canvas(file_path)
            pdf.drawString(100, 800, self.text_area.get(1.0, "end"))
            pdf.save()
            messagebox.showinfo("Export to PDF", "File successfully exported to PDF!")

    def make_bold(self):
        current_font = font.Font(font=self.text_area["font"])
        new_weight = "bold" if current_font.actual()["weight"] != "bold" else "normal"
        self.text_area.configure(font=(current_font.actual()["family"], current_font.actual()["size"], new_weight))

    def make_italic(self):
        current_font = font.Font(font=self.text_area["font"])
        new_slant = "italic" if current_font.actual()["slant"] != "italic" else "roman"
        self.text_area.configure(font=(current_font.actual()["family"], current_font.actual()["size"], new_slant))

    def make_underline(self):
        current_font = font.Font(font=self.text_area["font"])
        new_underline = 1 if current_font.actual()["underline"] == 0 else 0
        self.text_area.configure(font=(current_font.actual()["family"], current_font.actual()["size"], new_underline))

    def zoom_in(self):
        current_font = font.Font(font=self.text_area["font"])
        new_size = current_font.actual()["size"] + 2
        self.text_area.configure(font=(current_font.actual()["family"], new_size))

    def zoom_out(self):
        current_font = font.Font(font=self.text_area["font"])
        new_size = max(8, current_font.actual()["size"] - 2)
        self.text_area.configure(font=(current_font.actual()["family"], new_size))

    def find_and_replace(self):
        find_replace_window = Toplevel(self.master)
        find_replace_window.title("Find and Replace")
        find_replace_window.geometry("400x200")

        Label(find_replace_window, text="Find:").pack(pady=5)
        find_entry = Entry(find_replace_window, width=30)
        find_entry.pack(pady=5)

        Label(find_replace_window, text="Replace:").pack(pady=5)
        replace_entry = Entry(find_replace_window, width=30)
        replace_entry.pack(pady=5)

        Button(find_replace_window, text="Replace All",
               command=lambda: self.replace_text(find_entry.get(), replace_entry.get())).pack(pady=10)

    def replace_text(self, find_text, replace_text):
        content = self.text_area.get(1.0, "end")
        content = content.replace(find_text, replace_text)
        self.text_area.delete(1.0, "end")
        self.text_area.insert(1.0, content)

    def word_count(self):
        content = self.text_area.get(1.0, "end").strip()
        words = len(content.split())
        characters = len(content)
        messagebox.showinfo("Word Count", f"Words: {words}\nCharacters: {characters}")

    def spell_check(self):
        content = self.text_area.get(1.0, "end").split()
        spell = SpellChecker()
        misspelled = spell.unknown(content)
        if misspelled:
            messagebox.showinfo("Spell Check", f"Misspelled Words:\n{', '.join(misspelled)}")
        else:
            messagebox.showinfo("Spell Check", "No spelling errors found!")

    def show_about(self):
        messagebox.showinfo("About WordApp", "WordApp: An advanced text editor built with Python and tkinter.")


# Run the application
if __name__ == "__main__":
    root = Tk()
    app = WordApp(root)
    root.mainloop()
