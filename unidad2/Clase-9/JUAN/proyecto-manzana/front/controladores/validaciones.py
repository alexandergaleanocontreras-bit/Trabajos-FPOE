import re


class Validaciones():

    @staticmethod
    def validarOpcion(valor, campo, opciones):
        if valor not in opciones:
            return campo + ": elija una opción de la lista."
        return None

    @staticmethod
    def validarDecimal(valor, campo, minimo, maximo):
        texto = valor.strip()
        if not re.fullmatch(r"[0-9]+(\.[0-9]{1,2})?", texto) or not minimo < float(texto) <= maximo:
            return (campo + ": debe ser un número mayor que " + str(minimo)
                    + " y hasta " + str(maximo) + ", con máximo 2 decimales (ej. 180.50).")
        return None

    @staticmethod
    def validarManzana(manzana):
        errores = [
            Validaciones.validarOpcion(manzana.forma.get(), "Forma", manzana.FORMAS),
            Validaciones.validarOpcion(manzana.tamano.get(), "Tamaño", manzana.TAMANOS),
            Validaciones.validarDecimal(manzana.peso_g.get(), "Peso (g)", 0, 1000),
            Validaciones.validarOpcion(manzana.color_cascara.get(), "Color de la cáscara", manzana.COLORES),
        ]
        return [error for error in errores if error]
