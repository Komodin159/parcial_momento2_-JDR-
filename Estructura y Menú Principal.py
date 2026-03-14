import pandas as pd

gastos = []

def menu():
    while True:
        print("\n" + "="*30)
        print("CONTROL DE GASTOS - VEHICULOS")
        print("-"*30)
        print("1. Registrar nuevo gasto")
        print("2. Ver lista de gasto")
        print("3. Calcular gasto")
        print("4. Buscar gasto")
        print("="*30)


if __name__=="__main__":
    menu()