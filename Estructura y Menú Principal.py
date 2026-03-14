import pandas as pd

gastos = []


def menu():
    while True:
        print("\n" + "=" * 30)
        print(" CONTROL DE GASTOS - VEHÍCULOS")
        print("=" * 30)
        print("1. Registrar nuevo gasto")
        print("2. Ver lista de gastos")
        print("3. Calcular totales")
        print("4. Buscar gasto")
        print("5. Salir")
        print("-" * 30)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n-> Opción en desarrollo (usar ramas)...")
        elif opcion == "2":
            print("\n-> Opción en desarrollo (usar ramas)...")
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()