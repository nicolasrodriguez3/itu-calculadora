from helpers.console_helpers import request_numbers


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

    try:
        return n1 / n2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return divide()
    