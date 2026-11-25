from controladores.comunicacion import Comunicacion, ErrorComunicacion

comunicacion = Comunicacion()
datos = {
    "forma": "redonda",
    "tamano": "mediano",
    "peso_g": 180.5,
    "color_cascara": "roja",
}

try:
    creada = comunicacion.crear("manzanas", datos)
    id = creada["id"]
    print("POST   creada con id", id)

    print("GET    hay", len(comunicacion.listar("manzanas")), "manzanas")
    print("GET    consultada:", comunicacion.consultar("manzanas", id)["forma"])

    datos["peso_g"] = 250
    print("PUT    peso_g:", comunicacion.reemplazar("manzanas", id, datos)["peso_g"])

    cambio = {"color_cascara": "verde"}
    print("PATCH  color_cascara:", comunicacion.modificar("manzanas", id, cambio)["color_cascara"])

    comunicacion.eliminar("manzanas", id)
    print("DELETE eliminada")
except ErrorComunicacion as error:
    print("Algo falló:", error)

try:
    comunicacion.consultar("manzanas", 999999)
except ErrorComunicacion as error:
    print("Código", error.codigo, "->", error)

try:
    datos["peso_g"] = -5
    comunicacion.crear("manzanas", datos)
except ErrorComunicacion as error:
    print("Código", error.codigo, "->", error)
