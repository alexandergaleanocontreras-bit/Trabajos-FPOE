import tkinter as tk
from interfaz import InterfazGorra

# Punto de entrada principal de la aplicacion
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGorra(root)
    root.mainloop()