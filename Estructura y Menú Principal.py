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


def buscar_gastos(lista_gastos):
    # 1. Pedimos la placa que queremos encontrar
    placa_buscada = input("\nIngrese la placa que desea buscar: ")

    # Variable para saber si encontramos al menos un gasto
    encontrado = False

    print(f"\n--- Resultados para la placa {placa_buscada} ---")

    # 2. Recorremos toda la lista
    for gasto in lista_gastos:
        # 3. El condicional IF: ¿La placa de esta ficha es igual a la que busco?
        if gasto["placa"] == placa_buscada:
            print(f"Concepto: {gasto['concepto']} | Valor: ${gasto['valor']}")
            encontrado = True  # Sí encontramos algo

    # Si el ciclo termina y 'encontrado' sigue siendo False, avisamos que no hay nada
    if not encontrado:
        print("No se encontraron gastos registrados para esta placa.")
    print("-----------------------------------------")

if __name__ == "__main__":
    menu()