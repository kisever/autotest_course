# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("divisible, divisor, result", [
    pytest.param(5, 0, ZeroDivisionError, marks=pytest.mark.skip("bad test")),
    pytest.param(5, 2, 2.5),
    pytest.param(-6, 2, -3),
    pytest.param(10, 5, 2, marks=pytest.mark.smoke),
    pytest.param(4, 4, 1)])
def test_division(divisible, divisor, result):
    assert all_division(divisible, divisor) == result
