from src.calculator import Calculator
import pytest
import allure

calc = Calculator()

# Testing divide method
@allure.feature('Calculator')
@allure.story('Division')
@allure.severity(allure.severity_level.CRITICAL)
def test_divide():
    assert calc.divide(8, 2) == 4

@allure.feature('Calculator')
@allure.story('Division')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.parametrize('x,y,expected', [
    (10, 2, 5),
    (9, 3, 3),
    (-8, 4, -2),
    (0, 1, 0),
    (100, 10, 10)
])
def test_divide_normal(x, y, expected):
    assert calc.divide(x, y) == expected

@allure.feature('Calculator')
@allure.story('Division')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.xfail
@pytest.mark.parametrize('x,y,expected', [
    (None, None, ValueError),
    (10, None, ValueError),
    (None, 2, ValueError),
    (10, '2', ValueError),
    ('10', 2, ValueError),
    (10, 0, ValueError)
])
def test_divide_fail(x, y, expected):
    assert calc.divide(x, y) == expected
