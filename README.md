# Лабораторная работа №8 — Экосистемы Python

**ФИО:** Шкловский Герман Вячеславович  
**Группа:** 221141  
**Вариант:** 2  
**Номер лабораторной:** 8

## Задания варианта №2
- Среднее №2: зависимость `requests` в `pyproject.toml`, пример GET-запроса `fetch_status` с мок-тестом.
- Среднее №4: калькулятор с тестами `pytest` — сценарии TDD (функции `add`, `subtract`, `multiply`, `divide`).
- Среднее №7: модуль `logging` при выполнении вычислений.
- Повышенное №2: GitHub Actions CI запускает pytest при push/PR.
- Повышенное №6: Dockerfile для сборки и запуска приложения.

## Установка
```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m calculator
```
Требуется Python 3.11+.

## Docker
```bash
docker build -t lab08-variant2 .
docker run --rm lab08-variant2
```

## TDD
Тесты размещены в `tests/test_calculator.py`. Для демонстрации полного цикла Red-Green-Refactor необходимо показать историю коммитов с тестами до реализации; сам по себе конечный код не доказывает порядок разработки.

## Непрерывная интеграция
Workflow: `.github/workflows/tests.yml`. Статус проверок GitHub Actions смотри на вкладке Actions. Сборку Docker проверяют на компьютере с установленным Docker.
