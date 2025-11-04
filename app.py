import equipos
import jugadores
import partidos

def menu_principal():
    while True:
        print("""
=== LIGA DEPORTIVA AMATEUR ===
1. Gestión de equipos
2. Gestión de jugadores
3. Calendario y partidos
0. Salir
""")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            equipos.menu_equipos()
        elif opcion == "2":
            jugadores.menu_jugadores()
        elif opcion == "3":
            partidos.menu_partidos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()

