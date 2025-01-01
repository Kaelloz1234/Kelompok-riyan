from tkinter import *
from calculate import Calculator

class CalculatorGui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Scientific Calculator")
        
        # Set background color and prevent resizing
        self.root.configure(background="slategrey")  # Dark background
        self.root.resizable(width=False, height=False)
        self.root.geometry("800x600+400+100")  # Adjusted window size

        self.calc = Frame(self.root, bg="slategrey")
        self.calc.grid()

        self.textInput = StringVar()

        # Display configuration
        self.txtDisplay = Entry(self.calc, font=('arial', 20, 'bold'), textvariable=self.textInput, 
                                bg="#ecf0f1", bd=10, width=50, justify=RIGHT)
        self.txtDisplay.grid(row=0, column=0, columnspan=7, pady=20)
        self.txtDisplay.insert(0, "0")

        self.numbers = "789456123"

        # All buttons, including functions and numbers
        self.allcharacters = ["C", "CE", "√", "+", "π", "cos", "tan", 
                              "7", "8", "9", "-", "sin", "cosh", "tanh", 
                              "4", "5", "6", "*", "sinh", "exp", "mod",
                              "1", "2", "3", "/", "%", "deg", "log",
                              "0", ".", "±", "=", "log10", "x!", "e"]

    def init_calc_window(self):
        calculator = Calculator()
        i = 0
        btn = []

        # Generate buttons dynamically
        for j in range(2, 7):
            for k in range(7):
                btn_text = self.allcharacters[i]
                button = Button(self.calc, text=btn_text, width=5, height=2, font=('arial', 18, 'bold'), 
                                bd=4, relief=RAISED, bg="royalblue", fg="white", activebackground="gainsboro")
                
                button.grid(row=j, column=k, padx=10, pady=10)
                
                # Style specific buttons
                if btn_text not in self.numbers:
                    button.config(bg="navy")  # Non-number buttons have a red color
                
                # Set button command
                button['command'] = lambda x=btn_text: calculator.btn_click_func(x, self.textInput)
                i += 1

        self.root.mainloop()
