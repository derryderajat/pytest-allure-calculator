from src.calculator import Calculator
import pytest
import allure
calc = Calculator()

# Testing exponentiate method
@allure.feature('Calculator')
@allure.story('Exponentiation')
@allure.severity(allure.severity_level.CRITICAL)
def test_exponentiate():
    assert calc.exponentiate(2, 3) == 8

@allure.feature('Calculator')
@allure.story('Exponentiation')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.parametrize('base,exponent,expected', [
    (2, 3, 8),
    (3, 3, 27),
    (5, 0, 1),
    (10, 2, 100),
    (2, 10, 1024)
])
def test_exponentiate_normal(base, exponent, expected):
    assert calc.exponentiate(base, exponent) == expected

@allure.feature('Calculator')
@allure.story('Exponentiation')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.xfail
@pytest.mark.parametrize('base,exponent,expected', [
    (None, None, ValueError),
    (2, None, ValueError),
    (None, 3, ValueError),
    ('2', 3, ValueError),
    (2, '3', ValueError)
])
def test_exponentiate_fail(base, exponent, expected):
    assert calc.exponentiate(base, exponent) == expected

# Testing root method
@allure.feature('Calculator')
@allure.story('Root')
@allure.severity(allure.severity_level.CRITICAL)
def test_root():
    assert calc.root(4, 2) == 2