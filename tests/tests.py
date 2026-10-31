from UI.validations import *
from infrastructure.repository import *
from domain.complex_number import *
from business.service import *

def test_validations():
    """
    Functie care testeaza functiile validate_complex_number, validate_pos, validate_interval
    :return: None
    """
    r, i = validate_complex_number("3.5 -2.0")
    assert r == 3.5 and i == -2.0
    try:
        validate_complex_number("ab cd")
        assert False
    except ValueError:
        assert True

    assert validate_pos("2", 5) == 2
    try:
        validate_pos("5", 2)
        assert False
    except ValueError:
        assert True

    s, e = validate_interval("1 3", 5)
    assert s == 1 and e == 3

    assert validate_insert_pos("5", 6) == 5
    try:
        validate_insert_pos("5", 4)
        assert False
    except ValueError:
        assert True

    test_list = [complex_number(3.0, 5.0), complex_number(4.0, 2.0)]
    assert validate_num_is_in_list(test_list, complex_number(3.0, 5.0)) == True
    assert validate_num_is_in_list(test_list, complex_number(3.1, 4.0)) == False
def test_is_prime():
    """
    Functie care testeaza functia is_prime
    :return: None
    """
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(-5) == False
def test_complex_number_and_getters():
    """
    Functie care testeaza functiile complex_number, get_real, get_imag
    :return: None
    """
    z = complex_number(3.0, 5.0)
    assert get_real(z) == 3.0
    assert get_imag(z) == 5.0
def test_add_number():
    """
    Functie care testeaza functia add_number
    :return: None
    """
    test_list = []
    add_number(test_list, complex_number(3.0, 5.0))
    add_number(test_list, complex_number(4.0, 2.0))
    assert len(test_list) == 2
    assert get_real(test_list[0]) == 3.0
    assert get_imag(test_list[1]) == 2.0
def test_insert_at_pos():
    """
    Functie care testeaza functia insert_at_pos
    :return: None
    """
    test_list = []
    add_number(test_list, complex_number(3.0, 5.0))
    add_number(test_list, complex_number(4.0, 2.0))
    number = complex_number(7.0, 6.0)
    pos = 1
    insert_at_pos(test_list, number, pos)
    assert get_real(test_list[1]) == 7.0

def test_delete_number():
    """
    Functie care testeaza functia delete_number
    :return: None
    """
    test_list = [complex_number(3.0, 5.0), complex_number(4.0, 2.0)]
    delete_number_by_pos(test_list, 0)
    assert len(test_list) == 1
    assert get_real(test_list[0]) == 4.0
def test_delete_interval():
    test_list = [complex_number(3.0, 5.0),
                 complex_number(4.0, 2.0),
                 complex_number(6.0, 2.0)]
    delete_interval(test_list, (0, 1))
    assert len(test_list) == 1
def test_add_subseq():
    """
    Functie care testeaza functia add_subseq
    :return: None
    """
    test_list = [complex_number(3.0, 5.0),
                 complex_number(4.0, 2.0),
                 complex_number(6.0, 2.0)]
    sum_total = add_subseq(test_list, (0, 1))
    assert sum_total[0]== 7.0
    assert sum_total[1] == 7.0
def test_filter_real_prime():
    """
    Functie care testeaza functia filter_real_prime
    :return: None
    """
    test_list = [complex_number(2.0, 3.0),
                 complex_number(3.0, 2.0),
                 complex_number(-2.0, 3.0),
                 complex_number(5.2, 2.0)]
    filter_real_prime(test_list)
    assert len(test_list) == 2
    assert get_real(test_list[0]) == -2.0
    assert get_real(test_list[1]) == 5.2
def test_is_equal():
    """
    Functie care testeaza functia is_equal
    :return: None
    """
    assert is_equal(complex_number(3.0, 5.0), complex_number(3.0, 5.0))
def test_replace_number():
    """
    Functie care testeaza functia replace_number
    :return: None
    """
    test_list = [complex_number(3.0, 5.0),
                 complex_number(4.0, 2.0),
                 complex_number(6.0, 2.0)]
    replace_number(test_list, complex_number(3.0, 5.0), complex_number(1.0, 2.0))
    assert get_real(test_list[0]) == 1.0
def test_modulus():
    """
    Functie care testeaza functia modulus
    :return: None
    """
    assert modulus(complex_number(3.0, 4.0)) == 5.0
def test_modulus_less_than():
    """
    Functie care testeaza functia modulus_less_than
    :return: None
    """
    test_list = [complex_number(3.0, 5.0),
                 complex_number(4.0, 2.0),
                 complex_number(10.0, 5.0)]
    mod_list = modulus_less_than(test_list)
    assert len(mod_list) == 2
def test_modulus_equal_to():
    """
    Functie care testeaza functia modulus_equal_to
    :return: None
    """
    test_list = [complex_number(3.0, 5.0),
                 complex_number(8.0, 6.0),
                 complex_number(10.0, 0.0)]
    mod_list = modulus_equal_to(test_list)
    assert len(mod_list) == 2
def test_multuply():
    """
    Functie care testeaza functia multuply
    :return: None
    """
    num1 = complex_number(3.0, 5.0)
    num2 = complex_number(8.0, 6.0)
    prod = multiply(num1, num2)
    assert get_real(prod) == -6.0
    assert get_imag(prod) == 58.0
def test_interval_product():
    test_list = [complex_number(3.0, 5.0),
                 complex_number(4.0, 2.0),
                 complex_number(6.0, 2.0),
                 complex_number(10.0, 1.0)]
    prod = interval_product(test_list, (0, 2))
    assert get_real(prod) == -40.0
    assert get_imag(prod) == 160.0
def test_descending_sort_by_imag():
    """
    Functie care testeaza functia descending_sort_by_imag
    :return: None
    """
    test_list = [complex_number(3.0, 2.0),
                 complex_number(4.0, 1.0),
                 complex_number(6.0, 5.0),
                 complex_number(10.0, 2.0)]
    sorted_test_list = descending_sort_by_imag(test_list)
    assert get_imag(sorted_test_list[0]) == 5.0
    assert get_imag(sorted_test_list[1]) == 2.0
    assert get_imag(sorted_test_list[2]) == 2.0
    assert get_imag(sorted_test_list[3]) == 1.0
def test_filter_by_modulus():
    """
    Functie care testeaza functia filter_by_modulus
    :return:
    """
    test_list1 = [complex_number(3.0, 5.0),
                 complex_number(4.0, 2.0),
                 complex_number(6.0, 2.0),
                 complex_number(10.0, 2.0),
                 complex_number(6.0, 8.0)]
    test_list2 = test_list1.copy()
    test_list3 = test_list1.copy()
    filter_by_modulus(test_list1, 10.0, "<")
    filter_by_modulus(test_list2, 10.0, ">")
    filter_by_modulus(test_list3, 10.0, "=")
    assert len(test_list1) == 2
    assert len(test_list2) == 4
    assert len(test_list3) == 4
def test_undo():
    """
    Functie care testeaza functia undo
    :return: None
    """
    test_list = []
    test_history = []
    list_history(test_list, test_history)
    add_number(test_list, complex_number(3.0, 5.0))
    list_history(test_list, test_history)
    add_number(test_list, complex_number(4.0, 2.0))
    list_history(test_list, test_history)
    add_number(test_list, complex_number(6.0, 2.0))
    assert len(test_history) == 3
    undo(test_history, test_list)
    assert len(test_list) == 2
def test_history():
    """
    Functie care testeaza functia history
    :return: None
    """
    test_list = []
    test_history = []
    list_history(test_list, test_history)
    add_number(test_list, complex_number(3.0, 5.0))
    list_history(test_list, test_history)
    add_number(test_list, complex_number(4.0, 2.0))
    list_history(test_list, test_history)
    add_number(test_list, complex_number(6.0, 2.0))
    assert len(test_history) == 3
def test_all():
    """
    Functie care apeleaza toate functiile de test
    :return: None
    """
    test_validations()
    test_is_prime()
    test_complex_number_and_getters()
    test_add_number()
    test_delete_number()
    test_add_subseq()
    test_filter_real_prime()
    test_insert_at_pos()
    test_delete_interval()
    test_is_equal()
    test_replace_number()
    test_modulus()
    test_modulus_less_than()
    test_modulus_equal_to()
    test_multuply()
    test_interval_product()
    test_descending_sort_by_imag()
    test_filter_by_modulus()
    test_history()
    test_undo()