# lista que guarda todos los equipos en memoria
equipos = []

# funcion para generar id unico
def generar_id():
    if equipos:
        return equipos[-1]["id"] + 1
    else:
        return 1

# funcion para crear un equipo
def crear_equipo():
    print("\n--- crear equipo ---")
    nombre = input("nombre del equipo: ").strip()
    ciudad = input("ciudad: ").strip()

    if not nombre or not ciudad:
        print("error: nombre y ciudad no pueden estar vacios")
        return

    nuevo = {
        "id": generar_id(),
        "nombre": nombre,
        "ciudad": ciudad,
        "activo": True
    }

    equipos.append(nuevo)
    print("equipo creado correctamente")

# funcion para listar equipos activos
def listar_equipos():
    print("\n--- lista de equipos activos ---")
    activos = [e for e in equipos if e["activo"]]
    if not activos:
        print("no hay equipos activos")
        return
    tabla = [[e["id"], e["nombre"], e["ciudad"]] for e in activos]
    print(tabla, headers=["id", "nombre", "ciudad"], tablefmt="grid")

# funcion para buscar un equipo por id
def buscar_equipo():
    print("\n--- buscar equipo ---")
    try:
        id_buscar = int(input("id del equipo: "))
    except:
        print("id invalido")
        return

    for e in equipos:
        if e["id"] == id_buscar:
            print(f"id: {e['id']}")
            print(f"nombre: {e['nombre']}")
            print(f"ciudad: {e['ciudad']}")
            print(f"activo: {e['activo']}")
            return

    print("equipo no encontrado")

# funcion para actualizar datos de un equipo
def actualizar_equipo():
    print("\n--- actualizar equipo ---")
    try:
        id_act = int(input("id del equipo a actualizar: "))
    except:
        print("id invalido")
        return

    for e in equipos:
        if e["id"] == id_act:
            nuevo_nombre = input(f"nuevo nombre ({e['nombre']}): ").strip()
            nueva_ciudad = input(f"nueva ciudad ({e['ciudad']}): ").strip()

            if nuevo_nombre:
                e["nombre"] = nuevo_nombre
            if nueva_ciudad:
                e["ciudad"] = nueva_ciudad

            print("equipo actualizado")
            return

    print("equipo no encontrado")

# funcion para eliminar equipo (solo se marca como inactivo)
def eliminar_equipo():
    print("\n--- eliminar equipo ---")
    try:
        id_del = int(input("id del equipo a eliminar: "))
    except:
        print("id invalido")
        return

    for e in equipos:
        if e["id"] == id_del:
            e["activo"] = False
            print("equipo marcado como inactivo")
            return

    print("equipo no encontrado")

# menu del modulo de equipos
def menu_equipos():
    while True:
        print("\n--- menu de equipos ---")
        print("1. crear equipo")
        print("2. listar equipos")
        print("3. buscar equipo por id")
        print("4. actualizar equipo")
        print("5. eliminar equipo")
        print("0. volver al menu principal")

        opcion = input("elige una opcion: ")

        if opcion == "1":
            crear_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            buscar_equipo()
        elif opcion == "4":
            actualizar_equipo()
        elif opcion == "5":
            eliminar_equipo()
        elif opcion == "0":
            print("volviendo al menu principal...")
            break
        else:
            print("opcion no valida")


