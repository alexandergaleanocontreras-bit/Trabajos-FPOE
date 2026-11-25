import tkinter as tk


class Manzana():

    FORMAS = ["redonda", "ovalada", "conica", "achatada"]
    TAMANOS = ["pequeno", "mediano", "grande"]
    COLORES = ["roja", "verde", "amarilla", "bicolor"]

    def __init__(self, ventana_principal):
        self.id = None
        self.forma = tk.StringVar(ventana_principal)
        self.tamano = tk.StringVar(ventana_principal)
        self.peso_g = tk.StringVar(ventana_principal)
        self.color_cascara = tk.StringVar(ventana_principal)

    def cargar(self, datos):
        self.id = datos["id"]
        self.forma.set(datos["forma"])
        self.tamano.set(datos["tamano"])
        self.peso_g.set(datos["peso_g"])
        self.color_cascara.set(datos["color_cascara"])

    def limpiar(self):
        self.id = None
        self.forma.set("")
        self.tamano.set("")
        self.peso_g.set("")
        self.color_cascara.set("")

    def a_diccionario(self):
        return {
            "forma": self.forma.get(),
            "tamano": self.tamano.get(),
            "peso_g": round(float(self.peso_g.get().strip()), 2),
            "color_cascara": self.color_cascara.get(),
        }
