import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.current_number = tk.StringVar()
        self.current_number.set("0")

        self.display = tk.Entry(master, width=30, font=("Arial", 16), justify="right", textvariable=self.current_number)
        self.display.grid(columnspan=4, padx=5, pady=5)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.calculate_button = tk.Button(master, text="=", width=10, height=2, command=self.calculate)
        self.calculate_button.grid(row=5, column=2, columnspan=2)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=10, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.current_number.set("0")
        elif self.current_number.get() == "0":
            self.current_number.set(text)
        else:
            self.current_number.set(self.current_number.get() + text)

    def calculate(self):
        try:
            result = eval(self.current_number.get())
            self.current_number.set(result)
        except:
            self.current_number.set("ERROR")
    

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()