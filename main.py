from helpers.console_helpers import request_numbers


def main():
    while True:
        option: int = show_menu()

        match option:
            case 0:
                print("Gracias por usar el programa.")
                break
            case 1:
                print("El resultado es: ", add())
            case 2:
                print("El resultado es: ", subtract())
            case 3:
                print("El resultado es: ", multiply())
            case 4:
                print("El resultado es: ", divide())
            case _:
                print("Opcion inválida")


def add() -> float:
    n1, n2 = request_numbers()

    return n1 + n2


def subtract() -> float:
    n1, n2 = request_numbers()

    return n1 - n2


def multiply() -> float:
    n1, n2 = request_numbers()

    return n1 * n2


def divide() -> float:
    n1, n2 = request_numbers()

    return n1 / n2


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


if __name__ == "__main__":
    main()
