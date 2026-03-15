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

def calcular_gastos(lista_gastos):
    total_acumulado = 0.0
    for gasto_individual in lista_gastos:
        total_acumulado += gasto_individual["valor"]
    print(f"\nEl gasto total acumulado de todos los vehículos es: ${total_acumulado}")

if __name__ == "__main__":
    menu()