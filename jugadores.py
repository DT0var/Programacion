import equipos  

# lista que guarda todos los jugadores en memoria
jugadores = []

# funcion para generar id unico
def generar_id():
    if jugadores:
        return jugadores[-1]["id"] + 1
    else:
        return 1

# funcion para crear jugador
def crear_jugador():
    print("\n--- crear jugador ---")
    nombre = input("nombre del jugador: ").strip()
    posicion = input("posicion: ").strip()

    if not nombre or not posicion:
        print("error: nombre y posicion no pueden estar vacios")
        return

    try:
        id_equipo = int(input("id del equipo al que pertenece: "))
    except:
        print("id invalido")
        return

    # buscar equipo activo
    equipo = None
    for e in equipos.equipos:
        if e["id"] == id_equipo and e["activo"]:
            equipo = e
            break

    if not equipo:
        print("equipo no encontrado o inactivo")
        return

    nuevo = {
        "id": generar_id(),
        "nombre": nombre,
        "posicion": posicion,
        "id_equipo": id_equipo,
        "activo": True
    }

    jugadores.append(nuevo)
    print("jugador creado correctamente")

# funcion para listar jugadores activos
def listar_jugadores():
    print("\n--- lista de jugadores activos ---")
    activos = [j for j in jugadores if j["activo"]]
    if not activos:
        print("no hay jugadores activos")
        return

    # buscamos nombre del equipo de cada jugador
    tabla = []
    for j in activos:
        equipo = next((e["nombre"] for e in equipos.equipos if e["id"] == j["id_equipo"]), "sin equipo")
        tabla.append([j["id"], j["nombre"], j["posicion"], equipo])

    print(tabla, headers=["id", "nombre", "posicion", "equipo"], tablefmt="grid")

# funcion para buscar jugador por id
def buscar_jugador():
    print("\n--- buscar jugador ---")
    try:
        id_buscar = int(input("id del jugador: "))
    except:
        print("id invalido")
        return

    for j in jugadores:
        if j["id"] == id_buscar:
            equipo = next((e["nombre"] for e in equipos.equipos if e["id"] == j["id_equipo"]), "sin equipo")
            print(f"id: {j['id']}")
            print(f"nombre: {j['nombre']}")
            print(f"posicion: {j['posicion']}")
            print(f"equipo: {equipo}")
            print(f"activo: {j['activo']}")
            return

    print("jugador no encontrado")

# funcion para actualizar datos del jugador
def actualizar_jugador():
    print("\n--- actualizar jugador ---")
    try:
        id_act = int(input("id del jugador a actualizar: "))
    except:
        print("id invalido")
        return

    for j in jugadores:
        if j["id"] == id_act:
            nuevo_nombre = input(f"nuevo nombre ({j['nombre']}): ").strip()
            nueva_pos = input(f"nueva posicion ({j['posicion']}): ").strip()

            if nuevo_nombre:
                j["nombre"] = nuevo_nombre
            if nueva_pos:
                j["posicion"] = nueva_pos

            print("jugador actualizado")
            return

    print("jugador no encontrado")

# funcion para eliminar jugador (solo se marca como inactivo)
def eliminar_jugador():
    print("\n--- eliminar jugador ---")
    try:
        id_del = int(input("id del jugador a eliminar: "))
    except:
        print("id invalido")
        return

    for j in jugadores:
        if j["id"] == id_del:
            j["activo"] = False
            print("jugador marcado como inactivo")
            return

    print("jugador no encontrado")

# funcion para verificar si un equipo tiene jugadores (para modulo de equipos)
def equipo_tiene_jugadores(id_equipo):
    for j in jugadores:
        if j["id_equipo"] == id_equipo and j["activo"]:
            return True
    return False

# menu del modulo de jugadores
def menu_jugadores():
    while True:
        print("\n--- menu de jugadores ---")
        print("1. crear jugador")
        print("2. listar jugadores")
        print("3. buscar jugador por id")
        print("4. actualizar jugador")
        print("5. eliminar jugador")
        print("0. volver al menu principal")

        opcion = input("elige una opcion: ")

        if opcion == "1":
            crear_jugador()
        elif opcion == "2":
            listar_jugadores()
        elif opcion == "3":
            buscar_jugador()
        elif opcion == "4":
            actualizar_jugador()
        elif opcion == "5":
            eliminar_jugador()
        elif opcion == "0":
            print("volviendo al menu principal...")
            break
        else:
            print("opcion no valida")
