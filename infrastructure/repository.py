from domain.complex_number import get_real, get_imag
from math import sqrt
def is_prime(real_num):
    """
    Functie care verifica daca un numar este prim
    :param real_num: partea reala a unui numar complex
    :return: False - daca numarul nu este prim
             True - daca numarul este prim
    """
    if real_num < 2:
        return False
    elif real_num == 2:
        return True
    if real_num % 2 == 0:
        return False
    for i in range(3, int(real_num**0.5) + 1, 2):
        if real_num % i == 0:
            return False
    return True
def is_equal(complex_num1, complex_num2):
    """
    Functie care verifica daca 2 numere sunt egale
    :param complex_num1: nr complex
    :param complex_num2: nr complex
    :return: True - daca sunt egale
             False - altfel
    """
    if get_real(complex_num1) == get_real(complex_num2) and get_imag(complex_num1) == get_imag(complex_num2):
        return True
    return False
def modulus(num):
    """
    Functie care calucleaza modulul unui numar complex
    :param num: numar complex
    :return: modulul numarului complex
    """
    real = get_real(num)
    imag = get_imag(num)
    return sqrt(real**2 + imag**2)