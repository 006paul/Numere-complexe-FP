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
    sum_subseq = [0, 0]
    for i in range(interval[0], interval[1] + 1):
        imag_num = get_imag(numbers[i])
        real_num = get_real(numbers[i])
        sum_subseq[0] += real_num
        sum_subseq[1] += imag_num
    return sum_subseq
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
    """
    Functie care insereaza un numar complex num la pozitia pos
    :param numbers: lista de numere complexe
    :param number: numarul care se insereaza
    :param pos: pozitia la care se insereaza
    :return: None
    """
    numbers.insert(pos, number)
def delete_interval(numbers, interval):
    """
    Functie care elimina numerelor complexe din intervalul interval
    :param numbers: lista de numere complexe
    :param interval: intervalul din care se elimina numerele complexe
    :return: None
    """
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
        if modulus(num) == mod:
            mod_equal_to.append(num)
    return mod_equal_to
def interval_product(numbers, interval):
    """
    Functie care face produsul numerelor complexe din intervalul interval
    :param numbers: lista de numere complexe
    :param interval: intervalul in care se produsul numerelor complexe
    :return: prod - produsul nr complexe din intervalul interval
    """
    prod = {"real": 1.0,
            "imag": 0.0}
    for num in range(interval[0], interval[1] + 1):
        prod = multiply(prod, numbers[num])
    return prod
def descending_sort_by_imag(numbers):
    """
    Functie care sorteaza lista numbers descrescator dupa partea imaginara
    :param numbers: lista de numere complexes
    :return: sorted_list _ lista sortata
    """
    sorted_list = numbers.copy()
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if get_imag(sorted_list[i]) < get_imag(sorted_list[j]):
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    return sorted_list
def filter_by_modulus(numbers, mod, cmd):
    """
    Functie care filtreaza lista numbers in functie de modulul mod
    :param numbers: lista de numere complexe
    :param mod: modulul de comparatie
    :param cmd: proprietatea de comparatie
    :return: None
    """
    match cmd:
        case "<":
            filter_less_than(numbers, mod)
        case ">":
            filter_greater_than(numbers, mod)
        case "=":
            filter_equal_to(numbers, mod)
def undo(history, numbers):
    """
    Functie care reface ultima operatie efectuata asupra listei
    :param history: istoricul operatiilor facute asupra listei numbers
    :param numbers: lista de numere complexe
    :return: None
    """
    previous_state = history.pop()
    numbers.clear()
    numbers.extend(previous_state)