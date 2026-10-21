import tkinter as tk
from Gorra import Gorra

# Archivo de prueba basica para verificar la creacion del objeto
def test_objeto():
    root = tk.Tk()
    g = Gorra()
    print("Probando objeto Gorra...")
    print(g.mostrar_info())

if __name__ == "__main__":
    test_objeto()