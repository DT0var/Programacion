from datetime import datetime
import equipos  # Reutiliza el módulo 1

# Lista que guarda todos los partidos en memoria
partidos = []

# Función para generar ID único
def generar_id():
    if partidos:
        return partidos[-1]["id"] + 1
    return 1

# Función para crear un nuevo partido
def crear_partido():
    print("\n--- Crear partido ---")
    try:
        jornada = int(input("Número de jornada (≥1): "))
        if jornada < 1:
            print("La jornada debe ser mayor o igual a 1.")
            return
    except ValueError:
        print("Jornada inválida.")
        return

    try:
        local_id = int(input("ID del equipo local: "))
        visitante_id = int(input("ID del equipo visitante: "))
    except ValueError:
        print("ID de equipo inválido.")
        return

    if local_id == visitante_id:
        print("Error: un equipo no puede jugar contra sí mismo.")
        return

    # Validar que ambos equipos existan y estén activos
    local = next((e for e in equipos.equipos if e["id"] == local_id and e["activo"]), None)
    visitante = next((e for e in equipos.equipos if e["id"] == visitante_id and e["activo"]), None)

    if not local or not visitante:
        print("Uno o ambos equipos no existen o están inactivos.")
        return

    # Validar fecha y hora
    fecha_str = input("Fecha (AAAA-MM-DD): ").strip()
    hora_str = input("Hora (HH:MM): ").strip()

    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        datetime.strptime(hora_str, "%H:%M")
    except ValueError:
        print("Formato de fecha u hora inválido.")
        return

    # Evitar duplicar el mismo enfrentamiento en la misma jornada
    for p in partidos:
        if (
            p["jornada"] == jornada and
            ((p["local_id"] == local_id and p["visitante_id"] == visitante_id) or
             (p["local_id"] == visitante_id and p["visitante_id"] == local_id))
        ):
            print("Este enfrentamiento ya existe en esta jornada.")
            return

    nuevo = {
        "id": generar_id(),
        "jornada": jornada,
        "local_id": local_id,
        "visitante_id": visitante_id,
        "fecha": fecha_str,
        "hora": hora_str,
        "jugado": False,
        "resultado": None  # (golesLocal, golesVisitante)
    }

    partidos.append(nuevo)
    print(f"Partido creado: {local['nombre']} vs {visitante['nombre']} - Jornada {jornada}")

# Función para listar partidos
def listar_partidos():
    print("\n--- Listar partidos ---")
    filtro = input("¿Deseas filtrar por jornada? (s/n): ").strip().lower()

    if filtro == "s":
        try:
            jornada = int(input("Número de jornada: "))
        except ValueError:
            print("Jornada inválida.")
            return
        lista = [p for p in partidos if p["jornada"] == jornada]
    else:
        lista = partidos

    if not lista:
        print("No hay partidos para mostrar.")
        return

    tabla = []
    for p in lista:
        local = next((e["nombre"] for e in equipos.equipos if e["id"] == p["local_id"]), "Desconocido")
        visitante = next((e["nombre"] for e in equipos.equipos if e["id"] == p["visitante_id"]), "Desconocido")
        resultado = f"{p['resultado'][0]} - {p['resultado'][1]}" if p["resultado"] else "Pendiente"
        tabla.append([
            p["id"], p["jornada"], local, visitante, p["fecha"], p["hora"], 
            "Sí" if p["jugado"] else "No", resultado
        ])

    print(tabla, headers=[
        "ID", "Jornada", "Local", "Visitante", "Fecha", "Hora", "Jugado", "Resultado"
    ], tablefmt="grid")

# Reprogramar partido (solo si no se ha jugado)
def reprogramar_partido():
    print("\n--- Reprogramar partido ---")
    try:
        partido_id = int(input("ID del partido: "))
    except ValueError:
        print("ID inválido.")
        return

    partido = next((p for p in partidos if p["id"] == partido_id), None)
    if not partido:
        print("Partido no encontrado.")
        return

    if partido["jugado"]:
        print("No se puede reprogramar un partido ya jugado.")
        return

    nueva_fecha = input(f"Nueva fecha ({partido['fecha']}): ").strip()
    nueva_hora = input(f"Nueva hora ({partido['hora']}): ").strip()

    if nueva_fecha:
        try:
            datetime.strptime(nueva_fecha, "%Y-%m-%d")
            partido["fecha"] = nueva_fecha
        except ValueError:
            print("Fecha inválida. Se mantiene la anterior.")

    if nueva_hora:
        try:
            datetime.strptime(nueva_hora, "%H:%M")
            partido["hora"] = nueva_hora
        except ValueError:
            print("Hora inválida. Se mantiene la anterior.")

    print("Partido reprogramado correctamente.")

# Eliminar partido (solo si no se ha jugado)
def eliminar_partido():
    print("\n--- Eliminar partido ---")
    try:
        partido_id = int(input("ID del partido: "))
    except ValueError:
        print("ID inválido.")
        return

    partido = next((p for p in partidos if p["id"] == partido_id), None)
    if not partido:
        print("Partido no encontrado.")
        return

    if partido["jugado"]:
        print("No se puede eliminar un partido que ya se ha jugado.")
        return

    partidos.remove(partido)
    print("Partido eliminado correctamente.")

# Menú del módulo de partidos
def menu_partidos():
    while True:
        print("""
--- MENÚ DE CALENDARIO Y PARTIDOS ---
1. Crear partido
2. Listar partidos
3. Reprogramar partido
4. Eliminar partido
0. Volver al menú principal
""")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_partido()
        elif opcion == "2":
            listar_partidos()
        elif opcion == "3":
            reprogramar_partido()
        elif opcion == "4":
            eliminar_partido()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")
