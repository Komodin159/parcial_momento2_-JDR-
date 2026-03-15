gastos = []


def menu():
    while True:
        print("\n" + "=" * 30)
        print(" CONTROL DE GASTOS - VEHÍCULOS")
        print("=" * 30)
        print("1. Registrar nuevo gasto")
        print("2. Calcular total de gastos")
        print("3. Buscar gastos por placa")
        print("4. Salir")
        print("-" * 30)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gastos(gastos)

        elif opcion == "2":
            calcular_gastos(gastos)

        elif opcion == "3":
            buscar_gastos(gastos)

        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()