import tkinter as tk


class Gorra():

    def __init__(self, ventana_principal):
        self.id = None
        self.marca = tk.StringVar(ventana_principal)
        self.color = tk.StringVar(ventana_principal)
        self.precio = tk.StringVar(ventana_principal)
        self.stock = tk.StringVar(ventana_principal)

    def cargar(self, datos):
        self.id = datos['id']
        self.marca.set(datos['marca'])
        self.color.set(datos['color'])
        self.precio.set(str(datos['precio']))
        self.stock.set(str(datos['stock']))

    def limpiar(self):
        self.id = None
        self.marca.set('')
        self.color.set('')
        self.precio.set('')
        self.stock.set('')

    def a_diccionario(self):
        return {
            'marca': self.marca.get().strip(),
            'color': self.color.get().strip(),
            'precio': self.precio.get().strip(),
            'stock': int(self.stock.get().strip()),
        }