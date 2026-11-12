import tkinter as tk
from tkinter import messagebox
from controladores.validaciones import Validaciones
from controladores.comunicacion import Comunicacion, ErrorComunicacion
from modelos.gorra import Gorra

ROJO = '#b00020'

class Interfaz():

    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.gorra = Gorra(self.ventana_principal)
        self.comunicacion = Comunicacion()
        self.labels_error = []

    def al_soltar_tecla(self, validacion, label_error):
        label_error.config(text=validacion() or '')

    def accion_guardar(self):
        errores = Validaciones.validarGorra(self.gorra)
        if errores:
            messagebox.showwarning('Revise los datos', '\n'.join(errores))
            return

        try:
            creada = self.comunicacion.crear('gorras', self.gorra.a_diccionario())
        except ErrorComunicacion as error:
            messagebox.showerror('No se pudo guardar', str(error))
            return

        messagebox.showinfo(
            'Guardado',
            f"Gorra '{creada['marca']} - {creada['color']}' guardada con el ID {creada['id']}.",
        )
        self.accion_limpiar()

    def accion_limpiar(self):
        self.gorra.limpiar()
        for label_error in self.labels_error:
            label_error.config(text='')

    def al_cerrar(self):
        if messagebox.askyesno('Salir', '¿Seguro que quieres cerrar la aplicación?'):
            self.ventana_principal.destroy()

    def crear_campo(self, texto, variable, validacion):
        label = tk.Label(self.ventana_principal, text=texto)
        entry = tk.Entry(self.ventana_principal, textvariable=variable, width=35)
        label_error = tk.Label(self.ventana_principal, text='', fg=ROJO)
        entry.bind('<KeyRelease>', lambda evento: self.al_soltar_tecla(validacion, label_error))

        label.pack(anchor='w')
        entry.pack(anchor='w')
        label_error.pack(anchor='w')
        self.labels_error.append(label_error)

    def mostrar_interfaz(self):
        gorra = self.gorra
        self.ventana_principal.title('Gestión de Gorras')
        self.ventana_principal.geometry('360x380')
        self.ventana_principal.configure(padx=16, pady=12)

        self.crear_campo(
            'Marca', gorra.marca,
            lambda: Validaciones.validarTexto(gorra.marca.get(), 'Marca', 100),
        )
        self.crear_campo(
            'Color', gorra.color,
            lambda: Validaciones.validarTexto(gorra.color.get(), 'Color', 50),
        )
        self.crear_campo(
            'Precio (ej. 25000.00)', gorra.precio,
            lambda: Validaciones.validarDecimal(gorra.precio.get(), 'Precio'),
        )
        self.crear_campo(
            'Stock (Cantidad)', gorra.stock,
            lambda: Validaciones.validarEntero(gorra.stock.get(), 'Stock', 0),
        )

        boton_guardar = tk.Button(self.ventana_principal, text='Guardar', command=self.accion_guardar)
        boton_limpiar = tk.Button(self.ventana_principal, text='Limpiar', command=self.accion_limpiar)
        boton_guardar.pack(side='left', pady=10)
        boton_limpiar.pack(side='left', padx=8, pady=10)

        self.ventana_principal.protocol('WM_DELETE_WINDOW', self.al_cerrar)
        self.ventana_principal.mainloop()