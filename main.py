from typing import Any

import aritmetica as a
import palabras as p



def multiplicar(num1, num2):
    """
    Multiplica dos números enteros.

    :param num1: Número 1.
    :param num2: Número 2.

    :return: Producto de número 1 y número 2.
    """

    mult = num1*num2
    return mult


def es_palindromo(palabra):
    """
    Evalua si una palabra es un palíndromo.

    :param palabra: Palabra a evaluar.

    :return: `True` si la palabra es un palíndromo, `False` en caso contrario.
    """

    res = palabra[0:3]
    return res


def haz_algo_con(esto: str) -> Any:
    """
    Sé libre, haz algo con esto.

    :param esto: Algo.

    :return: ???
    """
    hola = esto
    return hola



if __name__ == "__main__":

    palabra = input("Introduce una palabra: ")
    while palabra == "":
        palabra = input("Error.\nIntroduce una palabra: ")

    while True:
        try:
            numero = int(input("Introduce un número: "))
            break
        except ValueError:
            print("Error.")

    print("La palabra tiene", p.longitud(palabra), "letras")

    if es_palindromo(palabra):
        print("La palabra es un palíndromo")

    print("La palabra invertida es", p.invertir(palabra))

    print("Y si escribieras", numero, "veces la palabra, escribirías", multiplicar(p.longitud(palabra), numero), "letras en total")

    print("Y ahora, como gran final...")

    haz_algo_con("esto")

