from tkinter import Tk, Label, Entry, Button, Text, END, filedialog, messagebox

class BillGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Generator")
        self.root.geometry("600x600")

        # Item Name
        Label(root, text="Item Name:", font=("Arial", 12)).place(x=30, y=30)
        self.item_name = Entry(root, font=("Arial", 12))
        self.item_name.place(x=150, y=30)

        # Quantity
        Label(root, text="Quantity:", font=("Arial", 12)).place(x=30, y=80)
        self.quantity = Entry(root, font=("Arial", 12))
        self.quantity.place(x=150, y=80)

        # Price
        Label(root, text="Price per Unit:", font=("Arial", 12)).place(x=30, y=130)
        self.price = Entry(root, font=("Arial", 12))
        self.price.place(x=150, y=130)

        # Add Button
        Button(root, text="Add Item", font=("Arial", 12), command=self.add_item).place(x=150, y=180)

        # Bill Area
        Label(root, text="Bill Details:", font=("Arial", 12, "bold")).place(x=30, y=240)
        self.bill_area = Text(root, font=("Courier", 12), width=60, height=20)
        self.bill_area.place(x=30, y=270)

        # Save Bill Button
        Button(root, text="Save Bill", font=("Arial", 12), command=self.save_bill).place(x=150, y=540)

        # Clear Bill Button
        Button(root, text="Clear Bill", font=("Arial", 12), command=self.clear_bill).place(x=250, y=540)

        # Initialize total
        self.total = 0.0
        self.bill_items = []

        self.generate_header()

    def generate_header(self):
        """Generates the bill header."""
        self.bill_area.insert(END, f"{'Item':<20}{'Quantity':<10}{'Price':<10}{'Total':<10}\n")
        self.bill_area.insert(END, "-" * 60 + "\n")

    def add_item(self):
        """Adds an item to the bill."""
        name = self.item_name.get().strip()
        quantity = self.quantity.get().strip()
        price = self.price.get().strip()

        if not name or not quantity or not price:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer and Price must be a number!")
            return

        total_price = quantity * price
        self.total += total_price
        self.bill_items.append((name, quantity, price, total_price))

        self.bill_area.insert(END, f"{name:<20}{quantity:<10}{price:<10}{total_price:<10.2f}\n")

        # Clear inputs
        self.item_name.delete(0, END)
        self.quantity.delete(0, END)
        self.price.delete(0, END)

    def save_bill(self):
        """Saves the bill to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not file_path:
            return

        with open(file_path, "w") as file:
            file.write(f"{'Item':<20}{'Quantity':<10}{'Price':<10}{'Total':<10}\n")
            file.write("-" * 60 + "\n")
            for item in self.bill_items:
                file.write(f"{item[0]:<20}{item[1]:<10}{item[2]:<10}{item[3]:<10.2f}\n")
            file.write("-" * 60 + "\n")
            file.write(f"{'Total:':<50}{self.total:<10.2f}\n")

        messagebox.showinfo("Success", "Bill saved successfully!")

    def clear_bill(self):
        """Clears the bill area and resets the total."""
        self.bill_area.delete(1.0, END)
        self.total = 0.0
        self.bill_items = []
        self.generate_header()

# Run the application
if __name__ == "__main__":
    root = Tk()
    app = BillGenerator(root)
    root.mainloop()
