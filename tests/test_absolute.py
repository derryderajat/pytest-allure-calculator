from src.calculator import Calculator
import pytest
import allure
calc = Calculator()
# Testing absolute method
def test_absolute():
    assert calc.absolute(-10) == 10

@allure.feature('Calculator')
@allure.story('Absolute')
@pytest.mark.smoke
@pytest.mark.parametrize('value,expected', [
    (10, 10),
    (-10, 10),
    (0, 0),
    (-999, 999),
    (12345, 12345)
])
def test_absolute_normal(value, expected):
    assert calc.absolute(value) == expected

@allure.feature('Calculator')
@allure.story('Absolute')
@pytest.mark.xfail
@pytest.mark.parametrize('value,expected', [
    (None, ValueError),
    ('10', ValueError),
    ('-10', ValueError),
    (None, ValueError)
])
def test_absolute_fail(value, expected):
    assert calc.absolute(value) == expected
