from infrastructure.repository import is_equal
def validate_complex_number(number_str):
    """
    Functie care valideaza daca un numar complex a fost introdus corect
    :param number_str: string - numar complex introdus de utilizator
    :return: tuplu (float, float) - partea reala si partea imaginara a numarului complex
    """
    nums = number_str.strip().split()
    if len(nums) != 2:
        raise ValueError("Trebuie sa introduceti exact doua numere (partea reala si parte imaginara)")
    try:
        real = float(nums[0])
        imag = float(nums[1])
        return real, imag
    except ValueError:
        raise ValueError("Valorile introduse trebuie sa fie numere")
def validate_insert_pos(pos_str, list_len):
    """
    Functie care valideaza pozitia pos
    :param pos_str: pozitia introdusa de utilizator pentru a insera un nr complex
    :param list_len: lungimea listei numbers
    :return: pos - pozitia pe care se insereaza un nr complex
    """
    try:
        pos = int(pos_str)
    except ValueError:
        raise ValueError("Pozitia trebuie sa fie un numar intreg")
    if pos < 0 or pos > list_len:
        raise ValueError(f"Pozitie invalida! Introduceti un numar intre 0 si {list_len}")
    return pos
def validate_pos(pos_str, list_len):
    """
    Functie care valideaza pozitia introdusa pos
    :param pos_str: pozitia introdusa de utilizator pentru a sterge un numar complex
    :param list_len: lungimea listei numbers
    :return: pos - pozitia de la care se sterge numarul complex din lista numbers
    """
    try:
        pos = int(pos_str)
    except ValueError:
        raise ValueError("Pozitia trebuie sa fie un numar intreg")
    if pos < 0 or pos >= list_len:
        raise ValueError(f"Pozitie invalida! Introduceti un numar intre 0 si {list_len - 1}")
    return pos
def validate_interval(interval_str, list_len):
    """
    Functie care valideaza un interval
    :param interval_str: intervalul care trebuie validat
    :param list_len: lungimea listei numbers
    :return: tuplu (int, int) - start, end
    """
    nums = interval_str.strip().split()
    if len(nums) != 2:
        raise ValueError("Trebuie sa introduceti exact doua numere intregi")
    try:
        start = int(nums[0])
        end = int(nums[1])
    except ValueError:
        raise ValueError("Pozitiile introduse trebuie sa fie numere intregi")
    if start < 0 or end >= list_len:
        raise ValueError("Pozitiile sunt in afara limitelor listei")
    if start > end:
        raise ValueError("Pozitia de inceput trebuie sa fie mai mica sau egala cu pozitia de sfarsit")
    return start, end
def validate_modulus(mod_str):
    """
    Functie care valideaza un modulul citit de la utilizator
    :param mod_str: modulul citit de la utilizator
    :return: mod - int
    """
    try:
        mod = float(mod_str)
    except ValueError:
        raise ValueError("Valoarea introdusa trebuie sa fie numar")

    if mod < 0:
        raise ValueError("Modulul trebuie sa fie un numar pozitiv")

    return mod
def validate_num_is_in_list(numbers, num):
    """
    Functie care verifica daca un numar este in lista
    :param num: numar complex
    :param numbers: lista de numere complexe
    :return: True - daca num este in lista
             False - altfel
    """
    for _num in numbers:
        if is_equal(_num, num):
            return True
    return False
def validate_undo(history):
    """
    Functie care valideaza daca se poate efectua undo
    :param history: istoricul operatiilor efectuate asupra listei numbers
    :return: True - daca se poate face undo
             False - altfel
    """
    if not history:
        return False
    return True