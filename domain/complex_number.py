def list_history(numbers, history):
    """
    Functie care salveaza lista numbers dupa fiecare operatie
    :param numbers: lista de numere complexe
    :return:
    """
    history.append(numbers.copy())
def complex_number(real, imag):
    """
    Functie care creeaza un numar complex
    :param real: partea reala a numarului complex
    :param imag: partea imaginara a numarului complex
    :return: dictionar in care cheia este partea reala si valoarea reprezinta partea imaginara
    """
    return {"real": real,
            "imag": imag}
def get_real(num):
    """
    Functie care extrage partea reala a numarului compex num
    :param num: numar complex
    :return: partea reala a numarului complex num
    """
    return num["real"]
def get_imag(num):
    """
    Functie care extrage partea imaginara a numarului complex num
    :param num: numar complex
    :return: partea imaginara a numarului complex num
    """
    return num["imag"]