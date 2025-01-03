import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Data Graph Maker")
        self.root.geometry("600x400")

        # Create widgets for user input and buttons
        self.create_widgets()

    def create_widgets(self):
        # Label and entry for sales data input
        self.data_label = tk.Label(self.root, text="Enter sales data (format: year,sales):")
        self.data_label.pack(pady=10)

        self.data_entry = tk.Entry(self.root, width=50)
        self.data_entry.pack(pady=10)

        self.plot_button = tk.Button(self.root, text="Plot Graph", command=self.plot_graph)
        self.plot_button.pack(pady=10)

        self.export_button = tk.Button(self.root, text="Export as PNG", command=self.export_graph)
        self.export_button.pack(pady=10)

        # Frame for displaying the graph
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack()

    def plot_graph(self):
        data = self.data_entry.get()
        if not data:
            messagebox.showerror("Input Error", "Please enter sales data.")
            return

        try:
            # Convert the input data into a pandas DataFrame
            data_list = [item.split(",") for item in data.split(";")]
            df = pd.DataFrame(data_list, columns=["Year", "Sales"])
            df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
            df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
            df.dropna(inplace=True)

            # Plot the graph
            fig, ax = plt.subplots()
            ax.plot(df["Year"], df["Sales"], marker='o')
            ax.set_title("Sales Data Over Years")
            ax.set_xlabel("Year")
            ax.set_ylabel("Sales")

            # Display the graph in the Tkinter window
            for widget in self.canvas_frame.winfo_children():
                widget.destroy()  # Clear previous graph

            self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()

        except Exception as e:
            messagebox.showerror("Data Error", f"Error processing data: {e}")

    def export_graph(self):
        data = self.data_entry.get()
        if not data:
            messagebox.showerror("Input Error", "Please enter sales data before exporting.")
            return

        try:
            data_list = [item.split(",") for item in data.split(";")]
            df = pd.DataFrame(data_list, columns=["Year", "Sales"])
            df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
            df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
            df.dropna(inplace=True)

            # Save the graph as a PNG
            fig, ax = plt.subplots()
            ax.plot(df["Year"], df["Sales"], marker='o')
            ax.set_title("Sales Data Over Years")
            ax.set_xlabel("Year")
            ax.set_ylabel("Sales")

            # Export to PNG
            fig.savefig("sales_graph.png")
            messagebox.showinfo("Export Success", "Graph exported as 'sales_graph.png'")

        except Exception as e:
            messagebox.showerror("Export Error", f"Error exporting graph: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
