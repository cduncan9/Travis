# test_calc


def test_add():
    from calc import add
    answer = add(4, 5)
    expected = 9
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
