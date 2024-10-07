def request_numbers() -> tuple[float, float]:
    try:
        n1 = float(input("Ingrese un número: "))
        n2 = float(input("Ingrese otro número: "))

        return n1, n2

    except ValueError:
        print("Por favor, solo ingrese números.")
        return request_numbers()


def show_menu() -> int:
    while True:
        print("0. Salir")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        try:
            return int(input("Ingrese una opcion: "))
        except ValueError:
            print("Opcion inválida")
        except KeyboardInterrupt:
            print("\n")
            return 0
