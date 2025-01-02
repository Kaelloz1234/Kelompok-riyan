from gui import CalculatorGui # ini buat import library CalculatorGui dari gui.py

# ini class buat manggil fungsi dari gui.py nampilin objek juga
class Main:
    def __init__(self):
        calculatorgui = CalculatorGui()
        calculatorgui.init_calc_window()

# nah ini buat nampilinnya
if __name__ == "__main__":
    Main()
    
# kalo mau buat aplikasinya, di terminal vscode input "pip install pyinstaller"
# matiin dulu real-time protection di windows ya
# di antivirus windowsnya pilih Add or remove exclusions, nanti pilih folder yang nyimpen 3 file ini
# nah terus input lagi di terminal "pyinstaller --onefile --windowed main.py"
# kalo mau buka aplikasinya, buka folde yg nyipen file ini terus buka folder "dist" 
# pilih deh main.exe
# gitu ya
