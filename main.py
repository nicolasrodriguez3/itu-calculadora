from typing import Generator


def main():
    while True:
        option: int = show_menu()
        
        match option:
            case 0:
                print("Gracias por usar el programa.")
                break
            case 1:
                print(add())
            case 2:
                subtract()
            case 3:
                multiply()
            case 4:
                divide()
            case _:
                print("Opcion inválida")
            
       
def add() -> float:
    n1 = float(input("Ingrese un número: "))
    n2 = float(input("Ingrese otro número: "))
    
    return n1 + n2
        
def subtract():
    pass
        
def multiply():
    pass
        
def divide():
    pass
        

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