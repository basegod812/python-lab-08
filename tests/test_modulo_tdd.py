"""Red stage for a new calculator feature: tests committed before implementation.

TDD history: this file is introduced while calculator.modulo does not exist.
"""
import pytest
from calculator import modulo


@pytest.mark.parametrize(
    "a,b,expected",
    [(10, 3, 1), (15, 5, 0), (-7, 3, 2)],
)
def test_modulo(a, b, expected):
    assert modulo(a, b) == expected


def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        modulo(4, 0)
