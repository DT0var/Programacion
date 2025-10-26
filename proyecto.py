# lista de articulos
articulos = []
# Funciones del programa
def generar_id():
    """Genera un ID automático."""
    if len(articulos) == 0:
        return 1
    else:
        return articulos[-1]["id"] + 1


def crear_articulo():
    print("\nCrear artículo")
    nombre = input("Nombre: ")
    while True:
        try:
            precio = float(input("Precio: "))
            break
        except:
            print("escribe un número válido.")
    while True:
        try:
            stock = int(input("Stock: "))
            break
        except:
            print("escribe un número entero.")
    nuevo = {"id": generar_id(), "nombre": nombre, "precio": precio, "stock": stock, "activo": True}
    articulos.append(nuevo)
    print("Artículo creado correctamente.\n")


def listar_articulos():
    print("\nLista de artículos")
    if len(articulos) == 0:
        print("No hay artículos registrados.")
    else:
        for a in articulos:
            estado = "Activo" if a["activo"] else "Inactivo"
            print(f"ID: {a['id']} | {a['nombre']} | Precio: {a['precio']} | Stock: {a['stock']} | {estado}")
        print()


def buscar_articulo_por_id(id_busqueda):
    for a in articulos:
        if a["id"] == id_busqueda:
            return a
    return None


def actualizar_articulo():
    print("\n--- Actualizar artículo ---")
    try:
        id_busqueda = int(input("ID del artículo: "))
    except:
        print("ID no válido.\n")
        return

    art = buscar_articulo_por_id(id_busqueda)
    if art:
        nuevo_nombre = input("Nuevo nombre (deja vacío para mantener): ")
        if nuevo_nombre != "":
            art["nombre"] = nuevo_nombre

        nuevo_precio = input("Nuevo precio (deja vacío para mantener): ")
        if nuevo_precio != "":
            try:
                art["precio"] = float(nuevo_precio)
            except:
                print("Precio no válido, no se cambió.")

        nuevo_stock = input("Nuevo stock (deja vacío para mantener): ")
        if nuevo_stock != "":
            try:
                art["stock"] = int(nuevo_stock)
            except:
                print("Stock no válido, no se cambió.")

        print("Artículo actualizado.\n")
    else:
        print("Artículo no encontrado.\n")


def eliminar_articulo():
    print("\n--- Eliminar artículo ---")
    try:
        id_busqueda = int(input("ID del artículo: "))
    except:
        print("ID no válido.\n")
        return

    art = buscar_articulo_por_id(id_busqueda)
    if art:
        articulos.remove(art)
        print("Artículo eliminado.\n")
    else:
        print("No encontrado.\n")


def alternar_activo():
    print("\n--- Cambiar activo/inactivo ---")
    try:
        id_busqueda = int(input("ID del artículo: "))
    except:
        print("ID no válido.\n")
        return

    art = buscar_articulo_por_id(id_busqueda)
    if art:
        art["activo"] = not art["activo"]
        estado = "activo" if art["activo"] else "inactivo"
        print(f"Artículo {art['nombre']} ahora está {estado}.\n")
    else:
        print("Artículo no encontrado.\n")


# Menú principal
def menu():
    opcion = 0
    while opcion != 7:
        print("=== MENÚ DE ARTÍCULOS ===")
        print("1. Crear artículo")
        print("2. Listar artículos")
        print("3. Buscar artículo por ID")
        print("4. Actualizar artículo")
        print("5. Eliminar artículo")
        print("6. Activar / Desactivar artículo")
        print("7. Salir")

        try:
            opcion = int(input("Elija una opción: "))
        except:
            opcion = 0

        if opcion == 1:
            crear_articulo()
        elif opcion == 2:
            listar_articulos()
        elif opcion == 3:
            try:
                id_busqueda = int(input("ID del artículo: "))
                art = buscar_articulo_por_id(id_busqueda)
                if art:
                    print(f"\n{art}\n")
                else:
                    print("\nNo encontrado.")
            except:
                print("ID no válido.\n")
        elif opcion == 4:
            actualizar_articulo()
        elif opcion == 5:
            eliminar_articulo()
        elif opcion == 6:
            alternar_activo()
        elif opcion == 7:
            print("\nvuelva pornto.")
        else:
            print("Opción no válida.\n")

menu()
