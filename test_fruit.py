import pytest


@pytest.mark.parametrize("in_fruit, expected", 
                         [("apple", True), 
                         ("banana ", True), 
                         ("wood", False)])
def test_is_fruit(in_fruit, expected):
    from fruit import is_fruit
    answer = is_fruit(in_fruit)
    assert answer == expected