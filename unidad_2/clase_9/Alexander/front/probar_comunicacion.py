from modelos.comunicacion import Comunicacion, ErrorComunicacion

comunicacion = Comunicacion()
datos = {
    'marca': 'Nike',
    'color': 'Negro',
    'precio': 45000.00,
    'stock': 12,
}

try:
    creada = comunicacion.crear('gorras', datos)
    id = creada['id']
    print('POST   creada con id', id)

    print('GET    hay', len(comunicacion.listar('gorras')), 'gorras')
    print('GET    consultada:', comunicacion.consultar('gorras', id)['marca'])

    datos['precio'] = 50000.00
    print('PUT    precio nuevo:', comunicacion.reemplazar('gorras', id, datos)['precio'])

    cambio = {'stock': 5}
    print('PATCH  stock nuevo:', comunicacion.modificar('gorras', id, cambio)['stock'])

    comunicacion.eliminar('gorras', id)
    print('DELETE eliminada')
except ErrorComunicacion as error:
    print('Algo falló:', error)

# Pruebas de errores a propósito
try:
    comunicacion.consultar('gorras', 999999)
except ErrorComunicacion as error:
    print('Código', error.codigo, '->', error)

try:
    datos['precio'] = -10
    comunicacion.crear('gorras', datos)
except ErrorComunicacion as error:
    print('Código', error.codigo, '->', error)