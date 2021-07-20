import allure


@allure.title('test_a')
def test_a():
    assert 1 + 2 == 3


@allure.title('test_b')
def test_b():
    assert 1 + 2 == 4


@allure.title('test_c')
def test_c():
    assert 1 + 2 == 3
