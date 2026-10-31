def complex_number(real, imag):
    """
    Functie care creeaza un numar complex
    :param real: partea reala a numarului complex
    :param imag: partea imaginara a numarului complex
    :return: lista in care primul el este partea reala, iar al doilea el este partea imaginara
    """
    return [real, imag]
def get_real(num):
    """
    Functie care extrage partea reala a numar compex
    :param num: numar complex
    :return: partea reala a numarului complex num
    """
    return num[0]
def get_imag(num):
    """
    Functie care extrage partea imaginara a numar complex
    :param num: numar complex
    :return: partea imaginara a numarului complex num
    """
    return num[1]