from gui import CalculatorGui # ini buat import library CalculatorGui dari gui.py

# ini class buat manggil fungsi dari gui.py nampilin objek juga
class Main:
    def __init__(self):
        calculatorgui = CalculatorGui()
        calculatorgui.init_calc_window()

# nah ini buat nampilinnya
if __name__ == "__main__":
    Main()
    
