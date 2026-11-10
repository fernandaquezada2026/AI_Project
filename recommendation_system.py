"""Sistema sencillo para recomendar productos según categorías favoritas."""


# Cada producto tiene un nombre y una o varias categorías.
productos = [
    {"nombre": "Auriculares inalámbricos", "categorias": ["tecnologia", "audio"]},
    {"nombre": "Libro de cocina", "categorias": ["libros", "cocina"]},
    {"nombre": "Altavoz portátil", "categorias": ["tecnologia", "audio"]},
    {"nombre": "Sartén antiadherente", "categorias": ["cocina", "hogar"]},
    {"nombre": "Novela de misterio", "categorias": ["libros", "ficcion"]},
]


def recomendar_productos(preferencias, catalogo, cantidad=3):
    """Devuelve hasta `cantidad` productos que coincidan con las preferencias."""
    if cantidad <= 0:
        return []

    recomendaciones = []

    # Cuenta cuántas categorías favoritas tiene cada producto.
    for producto in catalogo:
        coincidencias = 0
        for categoria in producto["categorias"]:
            if categoria in preferencias:
                coincidencias += 1

        # No recomienda productos que no tengan ninguna categoría favorita.
        if coincidencias > 0:
            recomendaciones.append((coincidencias, producto))

    # Ordena de más a menos coincidencias; mantiene el orden original en empates.
    recomendaciones.sort(key=lambda recomendacion: recomendacion[0], reverse=True)

    # Convierte la lista ordenada de pares en una lista de productos.
    resultado = []
    for puntuacion, producto in recomendaciones[:cantidad]:
        resultado.append(producto)

    return resultado


if __name__ == "__main__":
    # Cambia estas categorías para probar otras preferencias.
    preferencias_usuario = ["tecnologia", "audio"]
    sugerencias = recomendar_productos(preferencias_usuario, productos, cantidad=3)

    print("Productos recomendados:")
    for producto in sugerencias:
        print(f"- {producto['nombre']}")