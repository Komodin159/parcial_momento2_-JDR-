gastos = []


def registrar_gastos(lista_gastos):
    print("\n" + "-" * 25)
    print("NUEVO REGISTRO")
    print("-" * 25)

    while True:
        placa = input("Placa del vehículo: ").strip().upper()
        if 5 <= len(placa) <= 7:
            break
        print("Error: Ingrese una placa válida (5 a 7 caracteres).")

    while True:
        concepto = input("Concepto (Gasolina, Peaje, etc.): ").strip()
        if concepto != "":
            break
        print("Error: El concepto no puede estar vacío.")

    while True:
        try:
            valor = float(input("Valor del gasto: "))
            if valor >= 0:
                break
            print("Error: El valor no puede ser negativo.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    nuevo_gasto = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }
    lista_gastos.append(nuevo_gasto)
    print(f"\n¡Gasto registrado con éxito para la placa {placa}!")


def calcular_gastos(lista_gastos):
    total = 0.0
    for gasto in lista_gastos:
        total += gasto["valor"]
    print("\n" + "=" * 35)
    print(f"GASTO TOTAL DE LA EMPRESA: ${total:,.2f}")
    print("=" * 35)


def buscar_gastos(lista_gastos):
    placa_buscada = input("\nIngrese la placa a consultar: ").strip().upper()
    encontrado = False
    print(f"\nGastos encontrados para {placa_buscada}:")
    print("-" * 35)
    for gasto in lista_gastos:
        if gasto["placa"] == placa_buscada:
            print(f"Concepto: {gasto['concepto']} | Valor: ${gasto['valor']:,.2f}")
            encontrado = True
    if not encontrado:
        print("No se encontraron registros para esta placa.")
    print("-" * 35)


def menu():
    while True:
        print("═" * 33)
        print("  SISTEMA DE CONTROL DE GASTOS")
        print("═" * 33)
        print(" 1. Registrar gasto de vehículo")
        print(" 2. Calcular total acumulado   ")
        print(" 3. Buscar gastos por placa    ")
        print(" 4. Salir                      ")
        print("═" * 33)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gastos(gastos)
        elif opcion == "2":
            calcular_gastos(gastos)
        elif opcion == "3":
            buscar_gastos(gastos)
        elif opcion == "4":
            print("\nSaliendo del programa... ¡Feliz jornada!")
            break
        else:
            print("\nError: Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()