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