import tkinter as tk

class Manzana:
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.forma = tk.StringVar(ventanaPrincipal)
        self.tamano = tk.DoubleVar(ventanaPrincipal)
        self.peso = tk.IntVar(ventanaPrincipal)
        self.color_piel = tk.StringVar(ventanaPrincipal)

        self.forma.set("Redonda")
        self.tamano.set(5.0)
        self.peso.set(150)
        self.color_piel.set("Rojo")