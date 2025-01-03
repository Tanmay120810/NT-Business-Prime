import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from tkinter import ttk


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("800x600")
        self.root.config(bg="#f1f1f1")

        self.old_x = None
        self.old_y = None
        self.color = "black"
        self.brush_size = 5

        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=500)
        self.canvas.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        # Frame for tools
        tools_frame = tk.Frame(self.root, bg="#d3d3d3", height=100)
        tools_frame.pack(fill=tk.X)

        # Color Picker
        color_button = tk.Button(tools_frame, text="Color", command=self.choose_color, font=("Arial", 12), width=10, bg="#2d89e5", fg="white", relief="flat")
        color_button.pack(side=tk.LEFT, padx=10)

        # Brush Size Slider
        self.brush_slider = tk.Scale(tools_frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Brush Size", length=200, font=("Arial", 12))
        self.brush_slider.set(self.brush_size)
        self.brush_slider.pack(side=tk.LEFT, padx=10)

        # Clear Button
        clear_button = tk.Button(tools_frame, text="Clear", command=self.clear_canvas, font=("Arial", 12), width=10, bg="red", fg="white", relief="flat")
        clear_button.pack(side=tk.LEFT, padx=10)

        # Save Button
        save_button = tk.Button(tools_frame, text="Save", command=self.save_image, font=("Arial", 12), width=10, bg="#28a745", fg="white", relief="flat")
        save_button.pack(side=tk.LEFT, padx=10)

    def choose_color(self):
        color = colorchooser.askcolor()[1]  # Returns (rgb, hex)
        if color:
            self.color = color

    def draw(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=self.brush_size, fill=self.color, capstyle=tk.ROUND, smooth=True)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            try:
                # Saving canvas as image
                self.canvas.postscript(file=file_path + ".eps")
                messagebox.showinfo("Save", "Image saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save the image: {e}")

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)

    # Bind mouse events
    root.bind("<B1-Motion>", app.draw)
    root.bind("<ButtonRelease-1>", app.reset)

    root.mainloop()
