import tkinter as tk

class Gorra():

    def __init__(self, ventana_principal):
        self.marca = tk.StringVar(ventana_principal)
        self.color = tk.StringVar(ventana_principal)
        self.precio = tk.StringVar(ventana_principal)
        self.stock = tk.StringVar(ventana_principal)

    def limpiar(self):
        self.marca.set('')
        self.color.set('')
        self.precio.set('')
        self.stock.set('')

    def a_diccionario(self):
        return {
            'marca': self.marca.get().strip(),
            'color': self.color.get().strip(),
            'precio': float(self.precio.get().strip()),
            'stock': int(self.stock.get().strip()),
        }