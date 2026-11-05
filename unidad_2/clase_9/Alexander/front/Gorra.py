import tkinter as tk

# Clase principal que representa el objeto Gorra
class Gorra:
    def __init__(self):
        # Atributos vinculados a variables de Tkinter (StringVar)
        self.talla = tk.StringVar(value="M")
        self.visera = tk.StringVar(value="Plana")
        self.material = tk.StringVar(value="Algodon")
        self.cierre = tk.StringVar(value="Ajustable")

    # Metodo para formatear y retornar la informacion del objeto
    def mostrar_info(self):
        return f"Talla: {self.talla.get()}\nVisera: {self.visera.get()}\nMaterial: {self.material.get()}\nCierre: {self.cierre.get()}"