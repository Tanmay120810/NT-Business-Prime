import calendar
from tkinter import Tk, Label, Button, Spinbox, Frame, StringVar

class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar App")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        
        self.frame = Frame(master)
        self.frame.pack(pady=10)

        # Heading
        Label(self.frame, text="Calendar", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

        # Year input
        Label(self.frame, text="Year:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.year_var = StringVar(value="2025")
        self.year_spinbox = Spinbox(self.frame, from_=1900, to=2100, textvariable=self.year_var, width=8)
        self.year_spinbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Month input
        Label(self.frame, text="Month:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.month_var = StringVar(value="1")
        self.month_spinbox = Spinbox(self.frame, from_=1, to=12, textvariable=self.month_var, width=5)
        self.month_spinbox.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        # Display Button
        self.display_button = Button(self.frame, text="Show Calendar", command=self.show_calendar)
        self.display_button.grid(row=2, column=0, columnspan=4, pady=10)

        # Calendar Display
        self.calendar_label = Label(master, font=("Courier New", 10), justify="left", anchor="center", bg="white", relief="sunken")
        self.calendar_label.pack(fill="both", expand=True, padx=10, pady=10)

        self.show_calendar()

    def show_calendar(self):
        year = int(self.year_var.get())
        month = int(self.month_var.get())
        cal = calendar.TextCalendar(calendar.SUNDAY).formatmonth(year, month)
        self.calendar_label.config(text=cal)

# Run the Calendar App
if __name__ == "__main__":
    root = Tk()
    app = CalendarApp(root)
    root.mainloop()
