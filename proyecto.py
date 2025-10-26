#articulos u usuarios1
articulos = []
usuarios = []

def leer_entero(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("Debe escribir un número entero.")

def leer_flotante(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Debe escribir un número válido.")

def generar_id(lista):
    return lista[-1]["id"] + 1 if lista else 1

def validar_email(email):
    return "@" in email and "." in email

# Funciones genéricas
def listar_elementos(lista, campos):
    if not lista:
        print("No hay registros.\n")
        return
    for e in lista:
        datos = " | ".join([f"{c}: {e[c]}" for c in campos])
        estado = "Activo" if e["activo"] else "Inactivo"
        print(f"{datos} | {estado}")
    print()

def buscar_por_id(lista, id_busqueda):
    for e in lista:
        if e["id"] == id_busqueda:
            return e
    return None

def alternar_activo(lista, nombre):
    id_busqueda = leer_entero(f"ID del {nombre}: ")
    e = buscar_por_id(lista, id_busqueda)
    if e:
        e["activo"] = not e["activo"]
        estado = "activo" if e["activo"] else "inactivo"
        print(f"El {nombre} '{e['nombre']}' ahora está {estado}.\n")
    else:
        print(f"{nombre.capitalize()} no encontrado.\n")

#articulos
def crear_articulo():
    nombre = input("Nombre del artículo: ")
    precio = leer_flotante("Precio: ")
    stock = leer_entero("Stock: ")
    articulos.append({
        "id": generar_id(articulos),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    })
    print("Artículo creado.\n")

def actualizar_articulo():
    id_busqueda = leer_entero("ID del artículo: ")
    art = buscar_por_id(articulos, id_busqueda)
    if not art:
        print("Artículo no encontrado.\n")
        return
    nuevo_nombre = input("Nuevo nombre (vacío para mantener): ")
    if nuevo_nombre: art["nombre"] = nuevo_nombre
    nuevo_precio = input("Nuevo precio (vacío para mantener): ")
    if nuevo_precio:
        try: art["precio"] = float(nuevo_precio)
        except: print("Precio no válido.")
    nuevo_stock = input("Nuevo stock (vacío para mantener): ")
    if nuevo_stock:
        try: art["stock"] = int(nuevo_stock)
        except: print("Stock no válido.")
    print("Artículo actualizado.\n")

def eliminar_articulo():
    id_busqueda = leer_entero("ID del artículo: ")
    art = buscar_por_id(articulos, id_busqueda)
    if art:
        articulos.remove(art)
        print("Artículo eliminado.\n")
    else:
        print("Artículo no encontrado.\n")

def menu_articulos():
    while True:
        print("\n--- MENÚ DE ARTÍCULOS ---")
        print("1. Crear  2. Listar  3. Buscar  4. Actualizar")
        print("5. Eliminar  6. Activar/Desactivar  7. Volver")
        op = leer_entero("Opción: ")
        if op == 1: crear_articulo()
        elif op == 2: listar_elementos(articulos, ["id", "nombre", "precio", "stock"])
        elif op == 3:
            id_b = leer_entero("ID del artículo: ")
            print(buscar_por_id(articulos, id_b) or "No encontrado.\n")
        elif op == 4: actualizar_articulo()
        elif op == 5: eliminar_articulo()
        elif op == 6: alternar_activo(articulos, "artículo")
        elif op == 7: break
        else: print("Opción no válida.\n")

# usuarios
def crear_usuario():
    nombre = input("Nombre: ")
    email = input("Email: ")
    while not validar_email(email):
        print("Email no válido.")
        email = input("Email: ")
    usuarios.append({
        "id": generar_id(usuarios),
        "nombre": nombre,
        "email": email,
        "activo": True
    })
    print("Usuario creado.\n")

def actualizar_usuario():
    id_busqueda = leer_entero("ID del usuario: ")
    usr = buscar_por_id(usuarios, id_busqueda)
    if not usr:
        print("Usuario no encontrado.\n")
        return
    nuevo_nombre = input("Nuevo nombre (vacío para mantener): ")
    if nuevo_nombre: usr["nombre"] = nuevo_nombre
    nuevo_email = input("Nuevo email (vacío para mantener): ")
    if nuevo_email:
        if validar_email(nuevo_email): usr["email"] = nuevo_email
        else: print("Email no válido.")
    print("Usuario actualizado.\n")

def eliminar_usuario():
    id_busqueda = leer_entero("ID del usuario: ")
    usr = buscar_por_id(usuarios, id_busqueda)
    if usr:
        usuarios.remove(usr)
        print("Usuario eliminado.\n")
    else:
        print("Usuario no encontrado.\n")

def menu_usuarios():
    while True:
        print("\n--- MENÚ DE USUARIOS ---")
        print("1. Crear  2. Listar  3. Buscar  4. Actualizar")
        print("5. Eliminar  6. Activar/Desactivar  7. Volver")
        op = leer_entero("Opción: ")
        if op == 1: crear_usuario()
        elif op == 2: listar_elementos(usuarios, ["id", "nombre", "email"])
        elif op == 3:
            id_b = leer_entero("ID del usuario: ")
            print(buscar_por_id(usuarios, id_b) or "No encontrado.\n")
        elif op == 4: actualizar_usuario()
        elif op == 5: eliminar_usuario()
        elif op == 6: alternar_activo(usuarios, "usuario")
        elif op == 7: break
        else: print("Opción no válida.\n")

# menu
def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Artículos  2. Usuarios  3. Salir")
        op = leer_entero("Opción: ")
        if op == 1: menu_articulos()
        elif op == 2: menu_usuarios()
        elif op == 3:
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.\n")

# Ejecutar
menu_principal()
