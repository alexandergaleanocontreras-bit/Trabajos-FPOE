from tkinter import ttk

from controladores.validaciones import Validaciones
from modelos.manzana import Manzana
from vistas.vista_base import VistaBase


class VistaManzanas(VistaBase):

    titulo_formulario = "Datos de la manzana"
    recurso = "manzanas"
    columnas = (
        ("id", "Id", 50),
        ("forma", "Forma", 110),
        ("tamano", "Tamaño", 100),
        ("peso_g", "Peso (g)", 90),
        ("color_cascara", "Color de la cáscara", 150),
    )

    def crear_modelo(self):
        return Manzana(self)

    def crear_campos(self, marco):
        # Forma: lista desplegable
        combo_forma = ttk.Combobox(marco, textvariable=self.modelo.forma,
                                   values=Manzana.FORMAS, state="readonly", width=18)

        # Tamaño: botones de opción
        marco_tamano = ttk.Frame(marco)
        for tamano in Manzana.TAMANOS:
            ttk.Radiobutton(marco_tamano, text=tamano, value=tamano,
                            variable=self.modelo.tamano).pack(side="left", padx=(0, 6))

        # Peso: texto con expresión regular
        entry_peso = ttk.Entry(marco, textvariable=self.modelo.peso_g, width=20)

        # Color de la cáscara: selector con flechas
        spin_color = ttk.Spinbox(marco, textvariable=self.modelo.color_cascara,
                                 values=Manzana.COLORES, state="readonly", wrap=True, width=18)

        self.agregar_campo(marco, 0, 0, "Forma", combo_forma)
        self.agregar_campo(marco, 0, 2, "Tamaño", marco_tamano)
        self.agregar_campo(marco, 1, 0, "Peso en gramos (ej. 180.50)", entry_peso)
        self.agregar_campo(marco, 1, 2, "Color de la cáscara", spin_color)

    def validar(self):
        return Validaciones.validarManzana(self.modelo)

    def datos_formulario(self):
        return self.modelo.a_diccionario()

    def valores_fila(self, registro):
        return (
            registro["id"],
            registro["forma"],
            registro["tamano"],
            registro["peso_g"],
            registro["color_cascara"],
        )

    def texto_confirmar_eliminar(self, registro):
        return "¿Eliminar la manzana " + str(registro["id"]) + " (" + registro["forma"] + ", " + registro["color_cascara"] + ")?"
