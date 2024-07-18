from src.calculator import Calculator
import pytest
import allure
calc = Calculator()
# Testing root method
def test_root():
    assert calc.root(4, 2) == 2

@allure.feature('Calculator')
@allure.story('Root')
@pytest.mark.smoke
@pytest.mark.parametrize('value,degree,expected', [
    (4, 2, 2),
    (27, 3, 3),
    (81, 4, 3),
    (16, 2, 4),
    (256, 4, 4)
])
def test_root_normal(value, degree, expected):
    assert calc.root(value, degree) == expected

@allure.feature('Calculator')
@allure.story('Root')
@pytest.mark.xfail
@pytest.mark.parametrize('value,degree,expected', [
    (None, None, ValueError),
    (4, None, ValueError),
    (None, 2, ValueError),
    ('4', 2, ValueError),
    (4, '2', ValueError),
    (-4, 2, ValueError)
])
def test_root_fail(value, degree, expected):
    assert calc.root(value, degree) == expected

