gastos = []


def menu():
    while True:
        print("\n" + "=" * 30)
        print(" CONTROL DE GASTOS - VEHÍCULOS")
        print("=" * 30)
        print("1. Registrar nueva placa")
        print("2. Ver lista de gastos")
        print("3. Calcular gastos")
        print("4. Buscar gastos")
        print("5. Salir")
        print("-" * 30)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gastos(gastos)
        elif opcion == "2":
            print("\n-> Opción en desarrollo (usar ramas)...")
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def registrar_gastos(lista_gastos):

    placa = input("Ingrese la placa: ")
    concepto = input("Ingrese el concepto: ")
    valor = float(input("Ingrese el valor: "))

    nuevo_gasto = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }
    lista_gastos.append(nuevo_gasto)

    print(f"Gasto de la placa {placa} se registró con éxito")

if __name__ == "__main__":
    menu()