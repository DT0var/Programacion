# menu principal del proyecto liga deportiva amateur

import equipos
import jugadores

def menu_principal():
    while True:
        print("\n=== liga deportiva ===")
        print("1. gestion de equipos")
        print("2. gestion de jugadores")
        print("0. salir")

        opcion = input("elige una opcion: ")

        if opcion == "1":
            equipos.menu_equipos()
        elif opcion == "2":
            jugadores.menu_jugadores()
        elif opcion == "0":
            print("saliendo del programa...")
            break
        else:
            print("opcion no valida")

if __name__ == "__main__":
    menu_principal()
