import tkinter as tk
import math

class ScientificCalculator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Scientific Calculator")
        self.master.geometry("500x300")

        self.display = tk.Entry(self)
        self.display.grid(row=0, column=0, columnspan=5)

        self.buttons = {}
        for i in range(1, 10):
            self.buttons[str(i)] = tk.Button(self, text=str(i), command=lambda x=str(i): self.add_number(x))
            self.buttons[str(i)].grid(row=1 + i // 3, column=i % 3)

        self.buttons["."] = tk.Button(self, text=".", command=lambda: self.add_number("."))
        self.buttons["+"] = tk.Button(self, text="+", command=self.add_operator)
        self.buttons["-"] = tk.Button(self, text="-", command=self.add_operator)
        self.buttons["*"] = tk.Button(self, text="*", command=self.add_operator)
        self.buttons["/"] = tk.Button(self, text="/", command=self.add_operator)
        self.buttons["^"] = tk.Button(self, text="^", command=self.add_operator)
        self.buttons["pi"] = tk.Button(self, text="π", command=lambda: self.add_number("π"))
        self.buttons["e"] = tk.Button(self, text="e", command=lambda: self.add_number("e"))
        self.buttons["√"] = tk.Button(self, text="√", command=self.add_function)
        self.buttons["("] = tk.Button(self, text="(", command=self.add_parenthesis)
        self.buttons[")"] = tk.Button(self, text=")", command=self.add_parenthesis)
        self.buttons["="] = tk.Button(self, text="=", command=self.calculate)

        for row in range(2, 5):
            for col in range(3):
                self.buttons[chr(row + 64)] = tk.Button(self, text=chr(row + 64), command=lambda x=chr(row + 64): self.add_number(x))
                self.buttons[chr(row + 64)].grid(row=row, column=col)

    def add_number(self, number):
        self.display.insert("end", number)

    def add_operator(self):
        self.operator = self.buttons.get(self.display.get()[-1])
        self.display.delete(len(self.display.get()) - 1)

    def add_function(self):
        self.function = self.buttons.get(self.display.get()[-1])
        self.display.delete(len(self.display.get()) - 1)

    def add_parenthesis(self):
        self.parenthesis = self.buttons.get(self.display.get()[-1])
        self.display.delete(len(self.display.get()) - 1)

    def calculate(self):
        expression = self.display.get()
        try:
            result = eval(expression)
        except Exception as e:
            print(e)
            result = "Error"
        self.display.delete(0, len(expression))
        self.display.insert(0, result)

root = tk.Tk()
app = ScientificCalculator(root)
app.mainloop()
