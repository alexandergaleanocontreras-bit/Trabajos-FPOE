import re
import tkinter as tk
from tkinter import messagebox
from modelos.comunicacion import Comunicacion, ErrorComunicacion
from modelos.gorra import Gorra

ROJO = '#b00020'


class Interfaz():

    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.gorra = Gorra(self.ventana_principal)
        self.comunicacion = Comunicacion()

        self.talla = tk.StringVar(self.ventana_principal, value='M')
        self.visera = tk.StringVar(self.ventana_principal, value='Plana')
        self.material = tk.StringVar(self.ventana_principal, value='Algodon')
        self.cierre = tk.StringVar(self.ventana_principal, value='Snapback')

    def accion_guardar(self):
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
        material_texto = self.material.get().strip()

        if not re.match(patron, material_texto):
            messagebox.showerror('Error', 'El material debe tener solo letras')
            return

        self.gorra.marca.set(f"{self.cierre.get()} - Talla {self.talla.get()}")
        self.gorra.color.set(f"{material_texto} - Visera {self.visera.get()}")
        self.gorra.precio.set('35000')
        self.gorra.stock.set('1')

        try:
            creada = self.comunicacion.crear('gorras', self.gorra.a_diccionario())
        except ErrorComunicacion as error:
            messagebox.showerror('No se pudo guardar', str(error))
            return

        info = (
            f"Talla: {self.talla.get()}\n"
            f"Visera: {self.visera.get()}\n"
            f"Material: {material_texto}\n"
            f"Cierre: {self.cierre.get()}\n"
            f"ID en BD: {creada['id']}"
        )
        messagebox.showinfo('Datos Guardados', info)

    def al_cerrar(self):
        if messagebox.askyesno('Salir', '¿Seguro que quieres cerrar la aplicación?'):
            self.ventana_principal.destroy()

    def mostrar_interfaz(self):
        self.ventana_principal.title('Gorra - Registro')
        self.ventana_principal.geometry('350x300')

        tk.Label(self.ventana_principal, text='Talla:').grid(row=0, column=0, padx=15, pady=12, sticky='w')
        opciones_talla = ['S', 'M', 'L', 'XL']
        tk.OptionMenu(self.ventana_principal, self.talla, *opciones_talla).grid(row=0, column=1, padx=10, pady=12)

        tk.Label(self.ventana_principal, text='Visera:').grid(row=1, column=0, padx=15, pady=12, sticky='w')
        frame_radio = tk.Frame(self.ventana_principal)
        frame_radio.grid(row=1, column=1, padx=10, pady=12)
        tk.Radiobutton(frame_radio, text='Plana', variable=self.visera, value='Plana').pack(side='left')
        tk.Radiobutton(frame_radio, text='Curva', variable=self.visera, value='Curva').pack(side='left')

        tk.Label(self.ventana_principal, text='Material:').grid(row=2, column=0, padx=15, pady=12, sticky='w')
        tk.Entry(self.ventana_principal, textvariable=self.material).grid(row=2, column=1, padx=10, pady=12)

        tk.Label(self.ventana_principal, text='Cierre:').grid(row=3, column=0, padx=15, pady=12, sticky='w')
        opciones_cierre = ['Ajustable', 'Snapback', 'Cerrada']
        tk.OptionMenu(self.ventana_principal, self.cierre, *opciones_cierre).grid(row=3, column=1, padx=10, pady=12)

        btn = tk.Button(self.ventana_principal, text='Guardar', command=self.accion_guardar)
        btn.grid(row=4, column=0, columnspan=2, pady=18)

        self.ventana_principal.protocol('WM_DELETE_WINDOW', self.al_cerrar)
        self.ventana_principal.mainloop()