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
def calcular_gastos(lista_gastos):
    total_acumulado = 0.0
    for gasto_individual in lista_gastos:
        total_acumulado += gasto_individual["valor"]
    print(f"\nEl gasto total acumulado de todos los vehículos es: ${total_acumulado}")

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