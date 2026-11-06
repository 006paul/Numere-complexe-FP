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
    epsilon = 0.000000001
    if (get_real(complex_num1) + epsilon == get_real(complex_num2) + epsilon
        and get_imag(complex_num1) + epsilon == get_imag(complex_num2) + epsilon):
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
def multiply(num1, num2):
    """
    Functie care inmulteste doua numere complexe
    :param num1: nr complex
    :param num2: nr comlplex
    :return: product - num1*num2
    """
    t1 = get_real(num1) * get_real(num2)
    t2 = get_real(num1) * get_imag(num2)
    t3 = get_imag(num1) * get_real(num2)
    t4 = get_imag(num1) * get_imag(num2)
    product_real = t1 - t4
    product_imag = t2 + t3
    product = {"real": product_real,
               "imag": product_imag}
    return product
def filter_less_than(numbers, mod):
    """
    Functie care elimina din lista numbers numerele cu modul mai mic decat mod
    :param numbers: lista de numere complexe
    :param mod: modulul fata de care se face comparatia
    :return: None
    """
    i = len(numbers) - 1
    while i >= 0:
        if modulus(numbers[i]) < mod:
            numbers.pop(i)
        i -= 1
def filter_greater_than(numbers, mod):
    """
    Functie care elimina din lista numbers numerele cu modul mai mare decat mod
    :param numbers: lista de numere complexe
    :param mod: modulul fata de care se face comparatia
    :return: None
    """
    i = len(numbers) - 1
    while i >= 0:
        if modulus(numbers[i]) > mod:
            numbers.pop(i)
        i -= 1
def filter_equal_to(numbers, mod):
    """
    Functie care elimina din lista numbers numerele cu modul egal cu mod
    :param numbers: lista de numere complexe
    :param mod: modulul fata de care se face comparatia
    :return: None
    """
    i = len(numbers) - 1
    while i >= 0:
        if modulus(numbers[i]) == mod:
            numbers.pop(i)
        i -= 1