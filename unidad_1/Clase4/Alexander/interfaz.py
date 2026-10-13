import tkinter as tk
from tkinter import messagebox
import re
from Gorra import Gorra

# Clase para la ventana de la interfaz grafica
class InterfazGorra:
    def __init__(self, root):
        self.root = root
        self.root.title("Gorra - Registro")
        self.root.geometry("350x300")

        # Instancia del objeto Gorra para usar sus variables StringVar
        self.gorra = Gorra()

        self.crear_widgets()

    def crear_widgets(self):
        # 1. Campo Talla (Menu desplegable - OptionMenu)
        tk.Label(self.root, text="Talla:").grid(row=0, column=0, padx=10, pady=10)
        opciones_talla = ["S", "M", "L", "XL"]
        tk.OptionMenu(self.root, self.gorra.talla, *opciones_talla).grid(row=0, column=1)

        # 2. Campo Visera (Radiobuttons para seleccionar una opcion)
        tk.Label(self.root, text="Visera:").grid(row=1, column=0, padx=10, pady=10)
        frame_radio = tk.Frame(self.root)
        frame_radio.grid(row=1, column=1)
        tk.Radiobutton(frame_radio, text="Plana", variable=self.gorra.visera, value="Plana").pack(side="left")
        tk.Radiobutton(frame_radio, text="Curva", variable=self.gorra.visera, value="Curva").pack(side="left")

        # 3. Campo Material (Caja de texto Entry)
        tk.Label(self.root, text="Material:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.gorra.material).grid(row=2, column=1)

        # 4. Campo Cierre (Menu desplegable - OptionMenu)
        tk.Label(self.root, text="Cierre:").grid(row=3, column=0, padx=10, pady=10)
        opciones_cierre = ["Ajustable", "Snapback", "Cerrada"]
        tk.OptionMenu(self.root, self.gorra.cierre, *opciones_cierre).grid(row=3, column=1)

        # Boton para guardar los datos ingresados
        btn = tk.Button(self.root, text="Guardar", command=self.guardar)
        btn.grid(row=4, column=0, columnspan=2, pady=15)

    def guardar(self):
        # Expresion regular para validar que el material solo contenga letras
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$'
        
        # Validacion del campo material
        if not re.match(patron, self.gorra.material.get()):
            messagebox.showerror("Error", "El material debe tener solo letras")
            return

        # Si pasa la validacion, muestra la ventana emergente con los valores
        messagebox.showinfo("Datos Guardados", self.gorra.mostrar_info())