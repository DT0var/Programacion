import equipos

# Lista que guarda todos los jugadores en memoria
jugadores = []

# Función para generar ID único
def generar_id():
    if jugadores:
        return jugadores[-1]["id"] + 1
    return 1

# Alta de jugador
def crear_jugador():
    print("\n--- Alta de jugador ---")
    nombre = input("Nombre del jugador: ").strip()
    posicion = input("Posición: ").strip()

    if not nombre or not posicion:
        print("Error: nombre y posición no pueden estar vacíos.")
        return

    try:
        equipo_id = int(input("ID del equipo al que pertenece: "))
    except ValueError:
        print("ID inválido.")
        return

    # Validar que el equipo exista y esté activo
    equipo = next((e for e in equipos.equipos if e["id"] == equipo_id and e["activo"]), None)
    if not equipo:
        print("El equipo no existe o está inactivo.")
        return

    nuevo = {
        "id": generar_id(),
        "nombre": nombre,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "activo": True
    }
    jugadores.append(nuevo)
    print(f"Jugador '{nombre}' agregado correctamente al equipo '{equipo['nombre']}'.")

# Listar jugadores (todos o filtrados por equipo)
def listar_jugadores():
    print("\n--- Listar jugadores ---")
    filtro = input("¿Deseas filtrar por equipo? (s/n): ").strip().lower()

    if filtro == "s":
        try:
            equipo_id = int(input("ID del equipo: "))
        except ValueError:
            print("ID inválido.")
            return
        lista = [j for j in jugadores if j["equipo_id"] == equipo_id and j["activo"]]
    else:
        lista = [j for j in jugadores if j["activo"]]

    if not lista:
        print("No hay jugadores para mostrar.")
        return

    tabla = []
    for j in lista:
        equipo = next((e["nombre"] for e in equipos.equipos if e["id"] == j["equipo_id"]), "Sin equipo")
        tabla.append([j["id"], j["nombre"], j["posicion"], equipo])

    print(tabla, headers=["ID", "Nombre", "Posición", "Equipo"], tablefmt="grid")

# Buscar jugador por ID
def buscar_jugador():
    print("\n--- Buscar jugador por ID ---")
    try:
        jugador_id = int(input("ID del jugador: "))
    except ValueError:
        print("ID inválido.")
        return

    jugador = next((j for j in jugadores if j["id"] == jugador_id), None)
    if not jugador:
        print("Jugador no encontrado.")
        return

    equipo = next((e["nombre"] for e in equipos.equipos if e["id"] == jugador["equipo_id"]), "Sin equipo")

    print(f"""
Ficha del jugador:
------------------------
ID: {jugador['id']}
Nombre: {jugador['nombre']}
Posición: {jugador['posicion']}
Equipo: {equipo}
Activo: {"Sí" if jugador['activo'] else "No"}
""")

# Actualizar jugador
def actualizar_jugador():
    print("\n--- Actualizar jugador ---")
    try:
        jugador_id = int(input("ID del jugador a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    jugador = next((j for j in jugadores if j["id"] == jugador_id), None)
    if not jugador:
        print("Jugador no encontrado.")
        return

    nuevo_nombre = input(f"Nuevo nombre ({jugador['nombre']}): ").strip()
    nueva_posicion = input(f"Nueva posición ({jugador['posicion']}): ").strip()
    nuevo_equipo_id = input(f"Nuevo equipo ID ({jugador['equipo_id']}): ").strip()

    if nuevo_nombre:
        jugador["nombre"] = nuevo_nombre
    if nueva_posicion:
        jugador["posicion"] = nueva_posicion
    if nuevo_equipo_id:
        try:
            nuevo_equipo_id = int(nuevo_equipo_id)
            equipo = next((e for e in equipos.equipos if e["id"] == nuevo_equipo_id and e["activo"]), None)
            if equipo:
                jugador["equipo_id"] = nuevo_equipo_id
            else:
                print("El nuevo equipo no existe o está inactivo. Se mantiene el anterior.")
        except ValueError:
            print("ID de equipo inválido. Se mantiene el anterior.")

    print("Jugador actualizado correctamente.")

# Eliminar jugador
def eliminar_jugador():
    print("\nEliminar jugador")
    try:
        jugador_id = int(input("ID del jugador: "))
    except ValueError:
        print("ID inválido.")
        return

    jugador = next((j for j in jugadores if j["id"] == jugador_id), None)
    if not jugador:
        print("Jugador no encontrado.")
        return

    jugador["activo"] = False
    print(f"Jugador '{jugador['nombre']}' marcado como inactivo.")

# Menú del módulo de jugadores
def menu_jugadores():
    while True:
        print("""
--- MENÚ DE JUGADORES ---
1. Alta de jugador
2. Listar jugadores
3. Buscar jugador por ID
4. Actualizar jugador
5. Eliminar jugador (baja lógica)
0. Volver al menú principal
""")
        opcion = input("Elige una opción: ").strip()

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
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")
