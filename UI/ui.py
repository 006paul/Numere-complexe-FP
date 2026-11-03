from business.service import *
from UI.validations import *
def ui_menu():
    """
    Functie care afiseaza meniul principal
    :return: None
    """
    print("---------------------------------------------------------------------------------------\n"
          "Alegeti o comanda: \n"
          "1: Adauga numar complex la finalul listei \n"
          "2: Inserare numar complex pe o pozitie data \n"
          "3: Sterge element de pe o pozitie data \n"
          "4: Sterge elementele dintr-un interval \n"
          "5: Inlocuieste toate aparitiile unui numar cu un alt numar \n"
          "6: Afiseaza parte imaginara a numerelor complexe din lista \n"
          "7: Afiseaza numerele complexe care au modulul mai mic decat 10 \n"
          "8: Afiseaza numerele complexe care au modulul egal 10 \n"
          "9: Calculeaza suma numerelor dintr-o subsecventa \n"
          "10: Cacluleaza produsul numerelor dintr-o subsecventa \n"
          "11: Afiseaza lista sortata in ordine descrescatoare dupa partea imaginara \n"
          "12: Filtrare parte reala prim - elimina din lista numerele care au partea reala prim \n"
          "13: Elimina din lista numerele care au modulul <, >, = cu un numar dat \n"
          "14: Undo - Reface ultima operatie \n"
          "exit: Opreste programul \n"
          "---------------------------------------------------------------------------------------")
def ui_get_command():
    """
    Functie care citeste o comanda de la tastatura
    :return: command - string, comanda citita de la tastatura
    """
    command = input().strip()
    return command
def ui_show_command_prompt(command, numbers, history):
    """
    Functie care afiseaza un prompt pentru utilizator in functie de comanda selectata
    :param command: string, comanda citita de la tastatura
    :param numbers: lista de dictionare care contine numerele complexe introduse de utilizator
    :param history: istoricul operatiilor
    :return: None
    """
    if command == "1":
        num = ui_get_number("1")
        list_history(numbers, history)
        add_number(numbers, num)
        ui_print_list(numbers)
    if command == "2":
        pos = ui_get_insert_pos(len(numbers))
        if pos is not None:
            num = ui_get_number("1")
            if num is not None:
                list_history(numbers, history)
                insert_at_pos(numbers, num, pos)
                ui_print_list(numbers)
    if command == "3":
        pos = ui_get_delete_pos(len(numbers))
        if pos is not None:
            list_history(numbers, history)
            delete_number_by_pos(numbers, pos)
            ui_print_list(numbers)
    if command == "4":
        interval = ui_get_start_end(len(numbers))
        if interval is not None:
            list_history(numbers, history)
            delete_interval(numbers, interval)
            ui_print_list(numbers)
    if command == "5":
        num_to_replace = ui_get_num_from_list(numbers)
        if num_to_replace is not None:
            num_replace = ui_get_number("5")
            list_history(numbers, history)
            replace_number(numbers, num_to_replace, num_replace)
            ui_print_list(numbers)
    if command == "6":
        ui_print_imag_list(numbers)
    if command == "7":
        ui_print_list(modulus_less_than(numbers))
    if command == "8":
        ui_print_list(modulus_equal_to(numbers))
    if command == "9":
        interval = ui_get_start_end(len(numbers))
        if interval is not None:
            sum_subseq = add_subseq(numbers, interval)
            ui_print_subseq_sum(sum_subseq)
    if command == "10":
        interval = ui_get_start_end(len(numbers))
        if interval is not None:
            prod = interval_product(numbers, interval)
            ui_print_subseq_prod(prod)
    if command == "11":
        descending_sorted_numbers = descending_sort_by_imag(numbers)
        ui_print_list(descending_sorted_numbers)
    if command == "12":
        list_history(numbers, history)
        filter_real_prime(numbers)
        ui_print_list(numbers)
    if command == "13":
        cmd = ui_get_property()
        if cmd is not None:
            mod = ui_get_mod()
            if mod is not None:
                list_history(numbers, history)
                filter_by_modulus(numbers, mod, cmd)
                ui_print_list(numbers)
    if command == "14":
        if validate_undo(history):
            undo(history, numbers)
            ui_print_list(numbers)
        else:
            print("Nu se mai poate face undo")
def ui_get_mod():
    """
    Functie care citeste de la utuilator un numar - modulul unui nr complex
    :return: mod - string, modulul unui nr complex
    """
    while True:
        try:
            mod_str = input("Dati modulul: ").strip()
            mod = validate_modulus(mod_str)
            return mod
        except ValueError as e:
            print(f"Eroare: {e}")
def ui_get_property():
    """
    Functie care citeste semnul de comparatie de la utilizator (<,>,=)
    :return: cmd - string, semnul introdus de utilizator
    """
    while True:
        cmd = input("Dati proprietatea (<, >, =): ").strip()
        if cmd in ["<", ">", "="]:
            return cmd
        print("Comanda invalida")
def ui_print_list(numbers):
    """
    Functie care afiseaza lista curenta numbers - lista de stringuri care contine numere complexe
    :param numbers: lista de dictionare care contine numerele complexe introduse de utilizator
    :return: None
    """
    user_numbers = []
    for num in numbers:
        if get_imag(num) >= 0.0:
            user_numbers.append(f"{get_real(num)} + {get_imag(num)}i")
        else:
            user_numbers.append(f"{get_real(num)} - {abs(get_imag(num))}i")
    print(user_numbers)
def ui_print_imag_list(numbers):
    """
    Functie care afiseaza partea imaginara a numerelor din lista curenta numbers
    :param numbers: lista de numere complexe
    :return: None
    """
    imag_part = []
    for num in numbers:
        imag_part.append(get_imag(num))
    print(imag_part)
def ui_get_num_from_list(numbers):
    """
    Functie care citeste un numar complex de la utilizator care este deja in lista
    :return:
    """
    if len(numbers) == 0:
        print("Lista este goala!")
        return None
    while True:
        number = input("Dati numarul complex pentru inlocuit (parte reala si parte imaginara): ")
        try:
            real, imag = validate_complex_number(number)
            num = complex_number(real, imag)
            if validate_num_is_in_list(numbers, num):
                return num
            else:
                print("Numarul nu este in lista")
        except ValueError as e:
            print(f"Eroare: {e} Incercati din nou")
def ui_get_number(cmd):
    """
    Functie care citeste un numar complex de la tastatura
    :return: Un numar complex - dictionar in care cheia reprezinta partea reala a numarului complex,
             iar valoarea aferenta cheii reprezinta partea imaginara a numarului complex
    """
    while True:
        if cmd == "1":
            number = input("Dati numarul complex (parte reala si parte imaginara): ")
        elif cmd == "5":
            number = input("Dati numarul cu care va fi inlocuit numarul initial (parte reala si parte imaginara): ")
        try:
            real, imag = validate_complex_number(number)
            return complex_number(real, imag)
        except ValueError as e:
            print(f"Eroare: {e} Incercati din nou")
def ui_get_insert_pos(list_len):
    """
    Functie care citeste un nr intreg de la utilizator - pozitia pe care urmeaza a fi inserat un nr complex
    :param list_len: lungimea liste de numere complexe
    :return: pos - valida
             None - altfel
    """
    if list_len == 0:
        print("Lista este goala, numarul complex se va insera pe prima pozitie")
        return 0
    while True:
        pos_str = input(f"Dati pozitia (0 - {list_len - 1}): ")
        try:
            return validate_insert_pos(pos_str, list_len)
        except ValueError as e:
            print(f"Eroare: {e}")
def ui_get_delete_pos(list_len):
    """
    Functie care citeste de la utilizator un numar intreg - pozitia de pe care urmeaza a fi sters un numar complex
    :param list_len: lungimea listei de numere complexe
    :return: pos - valida
             None - atfel
    """
    if list_len == 0:
        print("Lista este goala, nu exista numere de sters")
        return None
    while True:
        pos_str = input(f"Dati pozitia (0 - {list_len - 1}): ")
        try:
            return validate_pos(pos_str, list_len)
        except ValueError as e:
            print(f"Eroare: {e}")
def ui_get_start_end(list_len):
    """
    Functie care citeste de la utilizator doua numere intregi - intervalul a carui suma urmeaza a fi calculata
    :param list_len: lungimea liste de numere complexe
    :return: tuplu (start_pos, end_pos) - index-urile pozitiilor de inceput si sfarsit al intervalului
    """
    if list_len == 0:
        print("Lista este goala")
        return None
    while True:
        interval = (input(f"Dati intervalul (0 - {list_len - 1}): "))
        try:
            return validate_interval(interval, list_len)
        except ValueError as e:
            print(f"Eroare: {e}")
def ui_print_subseq_sum(sum_subseq):
    """
    Functie care afiseaza suma numerelor complexe dintr-un interval
    :param sum_subseq: lista ce contine [suma_real, suma_imag]
    :return: None
    """
    if sum_subseq[1] >= 0.0:
        print(f"{sum_subseq[0]} + {sum_subseq[1]}i")
    else:
        print(f"{sum_subseq[0]} - {abs(sum_subseq[1])}i")
def ui_print_subseq_prod(prod):
    """
    Functie care afiseaza produsul numerelor complexe dintr-un intervalului
    :param prod: produsul numerelor complexe
    :return: None
    """
    if get_imag(prod) >= 0.0:
        print(f"{get_real(prod)} + {get_imag(prod)}i")
    else:
        print(f"{get_real(prod)} - {abs(get_imag(prod))}i")
def ui_run_command(command, numbers, history):
    """
    Functie care ruleaza comanda command
    :param numbers: lista de numere complexe
    :param command: string, comanda citita de la utilizator
    :param history: istoricul operatiilor
    :return: apeleaza functia ui_show_command_prompt, functie care afiseaza promptul aferent comenzii citite
    """
    commands = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    if command in commands:
        ui_show_command_prompt(command, numbers, history)
    else:
        print("Comanda invalida! Introduceti o comanda din meniu")