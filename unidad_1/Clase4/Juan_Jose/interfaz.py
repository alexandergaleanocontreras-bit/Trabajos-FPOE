import tkinter as tk
import re
from tkinter import messagebox, ttk

from Manzana import Manzana


class Interfaz:
    def __init__(self):
        self.ventanaPrincipal = tk.Tk()
        self.manzana = Manzana(self.ventanaPrincipal)

    def validar_tamano(self, valor):
        return re.fullmatch(r"\d*(?:[.,]\d{0,2})?", valor) is not None

    def validar_peso(self, valor):
        return re.fullmatch(r"\d*", valor) is not None

    def accion_guardar_boton(self):
        forma = self.manzana.forma.get().strip()
        tamano_texto = self.entrada_tamano.get().strip().replace(",", ".")
        peso_texto = self.entrada_peso.get().strip()
        color = self.manzana.color_piel.get()

        if not forma:
            messagebox.showwarning("Validación", "Selecciona la forma de la manzana.")
            return
        if not tamano_texto:
            messagebox.showwarning("Validación", "Ingresa el tamaño de la manzana.")
            return
        if re.fullmatch(r"\d+(?:\.\d{1,2})?", tamano_texto) is None:
            messagebox.showwarning("Validación", "Ingresa un tamaño numérico válido.")
            return
        if not peso_texto:
            messagebox.showwarning("Validación", "Ingresa el peso de la manzana.")
            return

        tamano = float(tamano_texto)
        peso = int(peso_texto)
        if not 0.1 <= tamano <= 20:
            messagebox.showwarning("Validación", "El tamaño debe estar entre 0.1 y 20 cm.")
            return
        if not 1 <= peso <= 1000:
            messagebox.showwarning("Validación", "El peso debe estar entre 1 y 1000 gramos.")
            return

        self.manzana.tamano.set(tamano)
        self.manzana.peso.set(peso)
        messagebox.showinfo(
            "Manzana guardada",
            f"Forma: {forma}\n"
            f"Tamaño: {tamano:g} cm\n"
            f"Peso: {peso} g\n"
            f"Color de piel: {color}",
        )

    def mostrar_interfaz(self):
        ventana = self.ventanaPrincipal
        manzana = self.manzana
        validar_tamano = (ventana.register(self.validar_tamano), "%P")
        validar_peso = (ventana.register(self.validar_peso), "%P")

        ventana.title("Registro de una manzana")
        ventana.resizable(False, False)

        ttk.Label(ventana, text="Forma:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        ttk.Combobox(
            ventana,
            textvariable=manzana.forma,
            values=("Redonda", "Ovalada", "Alargada"),
            state="readonly",
            width=18,
        ).grid(row=0, column=1, padx=10, pady=8)

        ttk.Label(ventana, text="Tamaño (cm):").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.entrada_tamano = tk.Spinbox(
            ventana,
            from_=0.1,
            to=20,
            increment=0.1,
            textvariable=manzana.tamano,
            validate="key",
            validatecommand=validar_tamano,
            width=18,
        )
        self.entrada_tamano.grid(row=1, column=1, padx=10, pady=8)

        ttk.Label(ventana, text="Peso (g):").grid(row=2, column=0, padx=10, pady=8, sticky="w")
        self.entrada_peso = ttk.Entry(
            ventana,
            textvariable=manzana.peso,
            validate="key",
            validatecommand=validar_peso,
            width=20,
        )
        self.entrada_peso.grid(row=2, column=1, padx=10, pady=8)

        ttk.Label(ventana, text="Color de piel:").grid(row=3, column=0, padx=10, pady=8, sticky="w")
        colores = ttk.Frame(ventana)
        colores.grid(row=3, column=1, padx=10, pady=8, sticky="w")
        for columna, color in enumerate(("Rojo", "Verde", "Amarillo")):
            ttk.Radiobutton(
                colores,
                text=color,
                value=color,
                variable=manzana.color_piel,
            ).grid(row=0, column=columna, padx=(0, 6))

        ttk.Button(ventana, text="Guardar", command=self.accion_guardar_boton).grid(
            row=4, column=0, columnspan=2, padx=10, pady=14
        )

        self.ventanaPrincipal.mainloop()