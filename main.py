from core.operations import add, subtract, multiply, divide
from helpers.console_helpers import show_menu


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

        print("")


if __name__ == "__main__":
    main()
