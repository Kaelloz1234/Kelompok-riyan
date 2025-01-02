import math

class Calculator: # buat class untuk diimport di gui.py
    def __init__(self):
        # ini variabel apa aja buat kalkulator scientificnya
        self.standardCalcCharacters = list('0123456789+-*/.')
        self.operatorCharacters = ['+', '-', '*', '/', '=', 'x!', '%']
        self.constantChars = ['π', 'e']
        self.operator, self.operatorDisplay = [], []
        self.oldBtnValue, self.oldBtnValueForDisplay, self.answer = '', '', ''

    # fungsi untuk input tombol dan memperbarui tampilan
    def btn_click_func(self, btnValue, textInput):
        # memeriksa apakah input sebelumnya itu '=' terus mengoperasikan input berikutnya
        if self.oldBtnValue == '=' and btnValue in self.operatorCharacters:
            self.operator, self.operatorDisplay = [self.answer], [self.answer]
        elif self.oldBtnValue == '=' and btnValue not in self.operatorCharacters:
            self.operatorDisplay = []

        # menggabungkan semua operator yang dimasukkin
        operatorStr = ''.join(self.operator)

        # ini button mapping scientifcnya supaya berfungsi 
        btn_map = {
            '√': ('math.sqrt(', '√'),
            'cos': ('math.cos(math.radians(', 'cos'),
            'sin': ('math.sin(math.radians(', 'sin'),
            'tan': ('math.tan(math.radians(', 'tan'),
            'cosh': ('math.cosh(math.radians(', 'cosh'),
            'sinh': ('math.sinh(math.radians(', 'sinh'),
            'tanh': ('math.tanh(math.radians(', 'tanh'),
            'exp': ('math.exp(', 'exp'),
            'log': ('math.log(', 'log'),
            'log10': ('math.log10(', 'log10')
        }

        # ini buat input button kalkukator scientificnya
        if btnValue in self.standardCalcCharacters:
            self._append_operator(btnValue)
        elif btnValue in btn_map:
            func, display = btn_map[btnValue]
            self._append_function(func, display, operatorStr)
        elif btnValue == 'mod':
            self._append_operator('%')
        elif btnValue == 'π':
            self._append_constant('math.pi', 'π', operatorStr)
        elif btnValue == 'e':
            self._append_constant('math.e', 'e', operatorStr)
        elif btnValue == '%':
            self._append_percentage(operatorStr)
        elif btnValue == 'x!':
            self._append_factorial(operatorStr)
        elif btnValue == '±':
            self._append_negate(operatorStr)
        elif btnValue == '=':
            self._calculate_result(operatorStr)
        elif btnValue == 'C':
            self._clear_last_entry()
        elif btnValue == 'CE':
            self._clear_all()

        # ini buat mengupdate tampilannya
        textInput.set(''.join(self.operatorDisplay))

    # menambahkan angka ke daftar operator sama display
    def _append_operator(self, value):
        self.oldBtnValue = self.oldBtnValueForDisplay = value
        self.operator.append(value)
        self.operatorDisplay.append(value)

    # menambahkan fungsi matematika cos, sin, dan log
    def _append_function(self, func, display, operatorStr):
        prefix = '*' if operatorStr.isdigit() else ''
        self.operator.append(prefix + func)
        self.operatorDisplay.append(prefix + display)

    # menambahkan konstanta π dan e 
    def _append_constant(self, func, display, operatorStr):
        prefix = '*' if operatorStr.isdigit() else ''
        self.operator.append(prefix + func)
        self.operatorDisplay.append(prefix + display)

    # ini buat hitung persentase dan dijadikan desimal angkanya
    def _append_percentage(self, operatorStr):
        if '(' in operatorStr:
            self.operator.append(operatorStr.count('(') * ')')
        self.operator = [operatorStr + '*0.01']
        self.operatorDisplay = [''.join(self.operatorDisplay) + '%']

    # menambahkan operasi faktorial ke ekspresinya
    def _append_factorial(self, operatorStr):
        if operatorStr.isdigit() or str(eval(operatorStr)).isdigit():
            self.operator = ['math.factorial(' + operatorStr]
            self.operatorDisplay.append('!')

    # ini negasi(-) untuk mengubah tanda angka
    def _append_negate(self, operatorStr):
        if '(' in operatorStr:
            self.operator.append(operatorStr.count('(') * ')')
        self.operator = ['-' + operatorStr]
        self.operatorDisplay = ['-' + ''.join(self.operatorDisplay)]

    # ini buat menghitung dan menampilkan hasilnya
    def _calculate_result(self, operatorStr):
        try:
            if '(' in operatorStr and ')' not in operatorStr:
                self.operator.append(operatorStr.count('(') * ')')
            self.answer = str(eval(''.join(self.operator)))
            self.operatorDisplay = [self.answer]
            self.operator, self.oldBtnValue = [], '='
        except: # nah ini kalo inputnya salah, nanti outputnya Error gini
            self.operatorDisplay, self.operator, self.oldBtnValue = ['Error'], [], '='

    # ini buat menghapus input yang terakhir
    def _clear_last_entry(self):
        if self.operator:
            self.operator.pop()
            self.operatorDisplay.pop()
            self.oldBtnValue = self.operator[-1] if self.operator else ''
            self.oldBtnValueForDisplay = self.operatorDisplay[-1] if self.operatorDisplay else ''

    # ini buat clear semua inputnya dan mengatur ulang kalkulator
    def _clear_all(self):
        self.operator, self.operatorDisplay, self.oldBtnValue, self.oldBtnValueForDisplay = [], [], '', ''
