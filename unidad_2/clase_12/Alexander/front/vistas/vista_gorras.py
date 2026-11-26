from tkinter import messagebox, ttk

from controladores.comunicacion import ErrorComunicacion
from controladores.validaciones import Validaciones
from modelos.gorra import Gorra
from vistas.vista_base import VistaBase


class VistaGorras(VistaBase):

    titulo_formulario = 'Datos de la gorra'
    recurso = 'gorras'
    columnas = (
        ('id', 'Id', 50),
        ('marca', 'Marca', 220),
        ('color', 'Color', 180),
        ('precio', 'Precio', 120),
        ('stock', 'Stock', 90),
    )

    def crear_modelo(self):
        return Gorra(self)

    def crear_campos(self, marco):
        entry_marca = ttk.Entry(marco, textvariable=self.modelo.marca)
        entry_color = ttk.Entry(marco, textvariable=self.modelo.color)
        entry_precio = ttk.Entry(marco, textvariable=self.modelo.precio)
        entry_stock = ttk.Entry(marco, textvariable=self.modelo.stock)

        self.agregar_campo(marco, 0, 0, 'Marca', entry_marca)
        self.agregar_campo(marco, 0, 2, 'Color', entry_color)
        self.agregar_campo(marco, 1, 0, 'Precio', entry_precio)
        self.agregar_campo(marco, 1, 2, 'Stock', entry_stock)

    def crear_botones_extra(self, marco):
        self.boton_stock = ttk.Button(marco, text='+1 Stock', command=self.accion_sumar_stock)
        self.boton_stock.pack(side='left', padx=(24, 0))

    def actualizar_botones(self):
        super().actualizar_botones()
        registro = self.registros.get(self.modelo.id)
        if registro is None:
            self.boton_stock.state(['disabled'])
        else:
            self.boton_stock.state(['!disabled'])

    def accion_sumar_stock(self):
        registro = self.registros[self.modelo.id]
        cambio = {'stock': registro['stock'] + 1}
        try:
            self.comunicacion.modificar(self.recurso, registro['id'], cambio)
        except ErrorComunicacion as error:
            messagebox.showerror('No se pudo actualizar el stock', str(error))
            return
        self.refrescar('Stock incrementado en 1 unidad.')

    def validar(self):
        return Validaciones.validarGorra(self.modelo)

    def datos_formulario(self):
        return self.modelo.a_diccionario()

    def valores_fila(self, registro):
        return (
            registro['id'],
            registro['marca'],
            registro['color'],
            registro['precio'],
            registro['stock'],
        )

    def texto_confirmar_eliminar(self, registro):
        return '¿Eliminar la gorra ' + registro['marca'] + ' (' + registro['color'] + ')?'