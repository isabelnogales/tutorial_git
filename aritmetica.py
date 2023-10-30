# Biblioteca de funciones aritméticas


def sumar(a: int, b: int) -> int:
    """
    Suma dos números enteros y devuelve el resultado

    :param a: Número A.
    :param b: Número B.

    :return: Suma de A y B.
    """
    suma = sum(a,b)
    return suma

def es_par(num: int) -> bool:
    """
    Evalua si un número es par.

    :param num: Número a evaluar.

    :return: `True` si es par, `False` en caso contrario.
    """

    if len(num) // 2:
        return True
    else:
        return False

