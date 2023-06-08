# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division



def test_all_division():
    assert all_division(10, 2) == 5


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)


@pytest.mark.smoke
def test_all_division_negative_numbers():
    assert all_division(-10, -2) == 5


def test_all_division_fractional_numbers():
    assert all_division(10, 0.5) == 20


def test_all_division_large_numbers():
    assert 10 == all_division(1000000, 100000)
