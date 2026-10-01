import tkinter as tk
import tkinter.messagebox as mesagebox
from unidad_1.Clase_4.Juan_Jose.Manzana import Manzana

class Interfaz:
    def __init__(self):
        self.ventanaPrincipal = tk.Tk()

    def accion_guardar_boton(self, forma):
        mesagebox.showinfo("Guardar", f"Guardando: forma: {forma}")

    def mostrar_interfaz(self):
        manzana = Manzana(self.ventanaPrincipal)

        labelforma = tk.Label(self.ventanaPrincipal, text="forma")
        entryforma = tk.Entry(self.ventanaPrincipal, textvariable=manzana.forma)

        boton_guardar = tk.Button(self.ventanaPrincipal,
                                   text="Guardar",
                                     command=lambda: self.accion_guardar_boton(manzana.forma.get()))

        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("300x300")
        labelforma.pack()
        entryforma.pack()
        boton_guardar.pack()
        
        self.ventanaPrincipal.mainloop()