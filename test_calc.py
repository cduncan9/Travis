# test_calc


import pytest


@pytest.mark.parametrize("add_1, add_2, expected",
                         [(1, 2, 3), (2, 2, 4), (3, 3, 6)])
def test_add(add_1, add_2, expected):
    from calc import add
    answer = add(add_1, add_2)
    assert answer == expected


def test_subtract():
    from calc import subtract
    answer = subtract(5, 4)
    expected = 1
    assert answer == expected


def test_multiply():
    from calc import multiply
    answer = multiply(4, 5)
    expected = 20
    assert answer == expected


def test_divide():
    from calc import divide
    answer = divide(4, 2)
    expected = 2
    assert answer == expected
