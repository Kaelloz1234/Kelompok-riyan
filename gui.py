from tkinter import *
from calculate import Calculator # ini buat import library Calculator yang ada di calculate.py

class CalculatorGui: #ini buat class supaya bisa dipake di main.py
    def __init__(self):
        self.root = Tk()
        self.root.title("Scientific Calculator")
        
        # bikin background
        self.root.configure(background="dimgrey")  # warna background
        self.root.resizable(width=False, height=False)
        self.root.geometry("780x620+400+100")  # background size

        self.calc = Frame(self.root, bg="dimgrey")
        self.calc.grid()

        self.textInput = StringVar()

        # display 
        self.txtDisplay = Entry(self.calc, font=('arial', 20, 'bold'), textvariable=self.textInput, 
                                bg="#ecf0f1", bd=10, width=50, justify=RIGHT)
        self.txtDisplay.grid(row=0, column=0, columnspan=7, pady=20)
        self.txtDisplay.insert(0, "0")

        self.numbers = "789456123"

        # ini buat menyatakan karakter dari tombolnya
        self.allcharacters = ["C", "CE", "√", "+", "π", "cos", "tan", 
                              "7", "8", "9", "-", "sin", "cosh", "tanh", 
                              "4", "5", "6", "*", "sinh", "exp", "mod",
                              "1", "2", "3", "/", "%", "deg", "log",
                              "0", ".", "±", "=", "log10", "x!", "e"]

    def init_calc_window(self):
        calculator = Calculator()
        i = 0
        btn = []

        # bikin buttonnya
        for j in range(2, 7):
            for k in range(7):
                btn_text = self.allcharacters[i]
                # ini buat button bagian angkanya dan background jika ditekan
                button = Button(self.calc, text=btn_text, width=5, height=2, font=('arial', 18, 'bold'), 
                                bd=4, relief=RAISED, bg="darkgray", fg="white", activebackground="gainsboro")
                
                button.grid(row=j, column=k, padx=10, pady=10)
                
                # style buat button bagian fungsi
                if btn_text not in self.numbers:
                    button.config(bg="darkorange") 
                
                # set button 
                button['command'] = lambda x=btn_text: calculator.btn_click_func(x, self.textInput)
                i += 1

        self.root.mainloop()
