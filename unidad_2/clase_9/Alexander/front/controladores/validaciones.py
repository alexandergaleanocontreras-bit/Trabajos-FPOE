import re

class Validaciones():

    @staticmethod
    def validarTexto(valor, campo, maximo):
        texto = valor.strip()
        if not texto:
            return f'{campo}: falta este dato.'
        if len(texto) > maximo:
            return f'{campo}: admite máximo {maximo} caracteres.'
        return None

    @staticmethod
    def validarEntero(valor, campo, minimo=0):
        texto = valor.strip()
        if not re.fullmatch(r'[0-9]+', texto) or int(texto) < minimo:
            return f'{campo}: debe ser un número entero mayor o igual a {minimo}.'
        return None

    @staticmethod
    def validarDecimal(valor, campo):
        texto = valor.strip()
        if not re.fullmatch(r'[0-9]+(\.[0-9]{1,2})?', texto):
            return f'{campo}: debe ser un número válido (ejemplo: 25000 o 25000.50).'
        try:
            if float(texto) <= 0:
                return f'{campo}: debe ser mayor a 0.'
        except ValueError:
            return f'{campo}: valor numérico no válido.'
        return None

    @staticmethod
    def validarGorra(gorra):
        errores = [
            Validaciones.validarTexto(gorra.marca.get(), 'Marca', 100),
            Validaciones.validarTexto(gorra.color.get(), 'Color', 50),
            Validaciones.validarDecimal(gorra.precio.get(), 'Precio'),
            Validaciones.validarEntero(gorra.stock.get(), 'Stock', 0),
        ]
        return [error for error in errores if error]