from domain.complex_number import *
from infrastructure.repository import *
def add_number(numbers, number):
    """
    Functie care adauga un numar complex la sfarsitul listei numbers
    :param numbers: lista de numere complexe
    :param number: numarul care urmeaza a fi adaugat
    :return: None
    """
    numbers.append(number)
def delete_number_by_pos(numbers, pos):
    """
    Functie care sterge un numar complex din lista numbers, de pe o anumita pozitie
    :param numbers: lista de numere complexe
    :param pos: pozitia de pe care urmeaza a fi sters numarul complex
    :return: None
    """
    numbers.pop(pos)
def add_subseq(numbers, interval):
    """
    Functie care calculeaza suma numerelor complexe din intervalul interval
    :param numbers: lista de numere complexe
    :param interval: intervalul in care se calculeaza suma numerelor complexe
    :return: sum - suma numerelor complexe din intervalul interval
    """
    sum = [0, 0]
    for i in range(interval[0], interval[1] + 1):
        imag_num = get_imag(numbers[i])
        real_num = get_real(numbers[i])
        sum[0] += real_num
        sum[1] += imag_num
    return sum
def filter_real_prime(numbers):
    """
    Functie care elimina din lista numbers numerele complexe ale caror parti reale sunt prime
    :param numbers: lista de numere complexe
    :return: None
    """
    i = len(numbers) - 1
    while i >= 0:
        real_num = get_real(numbers[i])
        if real_num == int(real_num):
            if is_prime(int(real_num)):
                numbers.pop(i)
        i -= 1
def insert_at_pos(numbers, number, pos):
    numbers.insert(pos, number)
def delete_interval(numbers, interval):
    del_interval = interval[1] - interval[0] + 1
    while del_interval > 0:
        numbers.pop(interval[0])
        del_interval -= 1
def replace_number(numbers, number_to_replace, num):
    """
    Functie care inlocuieste toate aparitiile unui nr cu un alt nr
    :param numbers: lista de numere complexe
    :param number_to_replace: numarul de inlocuit
    :param num: numarul cu care va fi inlocuit number_to_replace
    :return: None
    """
    for i in range(len(numbers)):
        if is_equal(numbers[i], number_to_replace):
            numbers[i] = num
def modulus_less_than(numbers, mod=10.0):
    """
    Functie care creeaza o lista cu numere complexe care au modulul mai mic decat 10
    :param numbers: lista de numere complexe
    :param mod: modulul de comparatie
    :return: mod_less_than - lista cu numere complexe care au modulul mai mic decat mod
    """
    mod_less_than = []
    for num in numbers:
        if modulus(num) < mod:
            mod_less_than.append(num)
    return mod_less_than
def modulus_equal_to(numbers, mod=10.0):
    """
    Functie care creeaza o lista cu numere complexe care au modulul egal cu 10
    :param numbers: lista de numere complexe
    :param mod: modulul de comparatie
    :return: mod_equal_to - lista cu numere complexe care au modulul egal cu 10
    """
    mod_equal_to = []
    for num in numbers:
        if modulus(num) == 10.0:
            mod_equal_to.append(num)
    return mod_equal_to