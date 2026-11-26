import re


class Validaciones():

    @staticmethod
    def validarGorra(gorra):
        errores = []

        marca = gorra.marca.get().strip()
        if not marca:
            errores.append('Marca: es obligatoria.')
        elif not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\-]+$', marca):
            errores.append('Marca: solo debe contener letras, números o guiones.')

        color = gorra.color.get().strip()
        if not color:
            errores.append('Color: es obligatorio.')
        elif not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s\-]+$', color):
            errores.append('Color: solo debe contener letras o espacios.')

        precio_txt = gorra.precio.get().strip()
        if not precio_txt:
            errores.append('Precio: es obligatorio.')
        else:
            try:
                precio = float(precio_txt)
                if precio <= 0:
                    errores.append('Precio: debe ser mayor a 0.')
            except ValueError:
                errores.append('Precio: debe ser un número válido.')

        stock_txt = gorra.stock.get().strip()
        if not stock_txt:
            errores.append('Stock: es obligatorio.')
        else:
            try:
                stock = int(stock_txt)
                if stock < 0:
                    errores.append('Stock: no puede ser negativo.')
            except ValueError:
                errores.append('Stock: debe ser un número entero.')

        return errores