"""ЛР №8: TDD-калькулятор и логирование. Тесты в tests/."""
import logging
import requests

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    logger.info("Складываем %s и %s", a, b)
    return a + b


def subtract(a: float, b: float) -> float:
    logger.info("Вычитаем %s из %s", b, a)
    return a - b


def multiply(a: float, b: float) -> float:
    logger.info("Умножаем %s на %s", a, b)
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено")
    logger.info("Делим %s на %s", a, b)
    return a / b


def fetch_status(url: str = "https://example.com") -> int:
    """Среднее №2: пример использования requests."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.status_code


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    print("Сумма:", add(2, 3))
    print("Частное:", divide(10, 2))


if __name__ == "__main__":
    main()
