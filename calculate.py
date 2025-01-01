import math

class Calculator:
    def __init__(self):

        self.standardCalcCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                    '+', '-', '*', '/', '.']
        self.operatorCharacters = ['+', '-', '*', '/', '=', 'x!', '%']

        self.constantChars = ["π", "e"]

        self.operator = [] 
        self.operatorDisplay = [] 
        self.oldBtnValue = '' 
        self.oldBtnValueForDisplay = '' # tampilan
        self.answer = '' # hasil 

    def btn_click_func(self, btnValue, textInput):
        
        # jika nilai btn sebelumnya "=" dan nilai btn sekarang di operatorCharacters, [result]
        # jkalo ga gini nanti yang di atas gak jalan
        if self.oldBtnValue == "=" and btnValue in self.operatorCharacters:

            self.operator = [self.answer]
            self.operatorDisplay = [self.answer]
        
        if self.oldBtnValue == "=" and btnValue not in self.operatorCharacters:
            self.operatorDisplay = []
        
        if btnValue in self.standardCalcCharacters:
            
            self.oldBtnValue = btnValue
            self.oldBtnValueForDisplay = btnValue
            self.operator.append(self.oldBtnValue)
            self.operatorDisplay.append(self.oldBtnValueForDisplay)
        else:
            operatorStr = ''.join(self.operator)
            if btnValue == '√':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.sqrt('
                    self.oldBtnValueForDisplay = '*√'
                else:
                    self.oldBtnValue = 'math.sqrt('
                    self.oldBtnValueForDisplay = '√'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            # sqrt √
            elif btnValue == 'cos':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.cos(math.radians('
                    self.oldBtnValueForDisplay = '*cos'
                else:
                    self.oldBtnValue = 'math.cos(math.radians('
                    self.oldBtnValueForDisplay = 'cos'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'tan':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.tan(math.radians('
                    self.oldBtnValueForDisplay = '*tan'
                else:
                    self.oldBtnValue = 'math.tan(math.radians('
                    self.oldBtnValueForDisplay = 'tan'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'sin':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.sin(math.radians('
                    self.oldBtnValueForDisplay = '*sin'
                else:
                    self.oldBtnValue = 'math.sin(math.radians('
                    self.oldBtnValueForDisplay = 'sin'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'cosh':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.cosh(math.radians('
                    self.oldBtnValueForDisplay = '*cosh'
                else:
                    self.oldBtnValue = 'math.cosh(math.radians('
                    self.oldBtnValueForDisplay = 'cosh'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'tanh':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.tanh(math.radians('
                    self.oldBtnValueForDisplay = '*tanh'
                else:
                    self.oldBtnValue = 'math.tanh(math.radians('
                    self.oldBtnValueForDisplay = 'tanh'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'sinh':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.sinh(math.radians('
                    self.oldBtnValueForDisplay = '*sinh'
                else:
                    self.oldBtnValue = 'math.sinh(math.radians('
                    self.oldBtnValueForDisplay = 'sinh'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'exp':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.exp('
                    self.oldBtnValueForDisplay = '*exp'
                else:
                    self.oldBtnValue = 'math.exp('
                    self.oldBtnValueForDisplay = 'exp'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'log':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.log('
                    self.oldBtnValueForDisplay = '*log'
                else:
                    self.oldBtnValue = 'math.log('
                    self.oldBtnValueForDisplay = 'log'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'log10':
                if operatorStr.isdigit() or self.oldBtnValue.isdigit() or self.oldBtnValueForDisplay in self.constantChars:
                    self.oldBtnValue = '*math.log10('
                    self.oldBtnValueForDisplay = '*log10'
                else:
                    self.oldBtnValue = 'math.log10('
                    self.oldBtnValueForDisplay = 'log10'
                
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            # ex: 8%3 = 2
            elif btnValue == 'mod':
                self.oldBtnValue = btnValue
                self.oldBtnValueForDisplay = btnValue
                self.operator.append("%")
                self.operatorDisplay.append("%")
            elif btnValue == 'π':
                if operatorStr.isdigit():
                    self.oldBtnValue = '*math.pi'
                    self.oldBtnValueForDisplay = '*π'
                else:
                    self.oldBtnValue = 'math.pi'
                    self.oldBtnValueForDisplay = 'π'

                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == 'e':
                if operatorStr.isdigit():
                    self.oldBtnValue = '*math.e'
                    self.oldBtnValueForDisplay = '*e'
                else:
                    self.oldBtnValue = 'math.e'
                    self.oldBtnValueForDisplay = 'e'
            
                self.operator.append(self.oldBtnValue)
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == '%':
                if "(" in operatorStr: 
                    num_parentheses = operatorStr.count('(')
                    self.operator.append(num_parentheses * ")")
                    operatorStr = ''.join(self.operator) # nyabung ke string baru

                self.oldBtnValue = operatorStr + "*0.01"
                self.oldBtnValueForDisplay = ''.join(self.operatorDisplay) + "%" # display
            
                self.operator = [self.oldBtnValue]
                self.operatorDisplay = [self.oldBtnValueForDisplay]

            elif btnValue == 'x!':
                if operatorStr.isdigit() or str(eval(operatorStr)).isdigit(): # faktorial buat bilangan bulat aja
                    self.oldBtnValue = "math.factorial(" + operatorStr
                    self.oldBtnValueForDisplay = '!'
            
                self.operator = [self.oldBtnValue]
                self.operatorDisplay.append(self.oldBtnValueForDisplay)
            elif btnValue == '±':
                if "(" in operatorStr: 
                    num_parentheses = operatorStr.count('(')
                    self.operator.append(num_parentheses * ")")
                    # tutup semua tanda kurung sebelum masukin minus, positif jadi negatif, negatif jadi positif
                    operatorStr = ''.join(self.operator) 

                self.oldBtnValue = "-" + operatorStr
                self.oldBtnValueForDisplay = '-' + ''.join(self.operatorDisplay) 
            
                self.operator = [self.oldBtnValue]
                self.operatorDisplay = [self.oldBtnValueForDisplay]
            elif btnValue == '=':
                try:
                    if "(" in operatorStr and ")" not in operatorStr:
                        num_parentheses = operatorStr.count('(')
                        self.operator.append(num_parentheses * ")")
                        operatorStr = ''.join(self.operator) # masuk string baru lg
                    
                    self.answer = str(eval(operatorStr))
                    self.operatorDisplay = [self.answer] # cuma 1 elemen jawaban
                    self.operator = [] 
                    self.oldBtnValue = "="
                except: 
                    self.operatorDisplay = ["Error"] # cuma 1 elemen jawaban
                    self.operator = []
                    self.oldBtnValue = "="
            elif btnValue == 'C':
                del self.operator[-1] 
                del self.operatorDisplay[-1]
                
                if self.operator: 
                    self.oldBtnValue = self.operator[-1]
                    self.oldBtnValueForDisplay = self.operatorDisplay[-1]
                else:
                    self.oldBtnValue = ''
                    self.oldBtnValueForDisplay = ''
            elif btnValue == 'CE': # clear
                self.operator = []
                self.operatorDisplay = []
            
        textInput.set(''.join(self.operatorDisplay)) # buat nampilin
