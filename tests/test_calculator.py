"""Тесты калькулятора: тестовые сценарии для подхода TDD."""
from unittest.mock import Mock, patch
import pytest
from calculator import add, subtract, multiply, divide, fetch_status


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(8, 2) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)


def test_requests_usage():
    with patch("calculator.requests.get") as get:
        response = Mock(status_code=200)
        get.return_value = response
        assert fetch_status("https://example.com") == 200
        get.assert_called_once_with("https://example.com", timeout=10)
