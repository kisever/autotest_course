import pytest
import datetime




@pytest.fixture()
def tests_timing():

    print()
    yield
    end = datetime.datetime.now()
    end = end.time()
    print((f'Прохождение тестов завершено в {end}'))


@pytest.fixture(autouse=True)
def test_time():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    time = end - start
    print(f'Время выполнения теста {time}')


