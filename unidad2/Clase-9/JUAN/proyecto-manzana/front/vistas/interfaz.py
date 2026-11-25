import tkinter as tk
from tkinter import messagebox, ttk

from controladores.comunicacion import Comunicacion
from vistas.vista_manzanas import VistaManzanas


class Interfaz():

    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.comunicacion = Comunicacion()

    def al_cerrar(self):
        if messagebox.askyesno("Salir", "¿Seguro que quieres cerrar la aplicación?"):
            self.ventana_principal.destroy()

    def mostrar_interfaz(self):
        ventana = self.ventana_principal
        ventana.title("Manzanas")
        ventana.geometry("720x520")
        ventana.minsize(640, 420)

        pestanas = ttk.Notebook(ventana)
        pestanas.pack(fill="both", expand=True)
        pestanas.add(VistaManzanas(pestanas, self.comunicacion), text="Manzanas")

        ventana.protocol("WM_DELETE_WINDOW", self.al_cerrar)
        ventana.mainloop()
