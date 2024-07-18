from src.calculator import Calculator
import pytest
import allure
calc = Calculator()
def test_subtract():
    assert calc.subtract(1,4) == -3


@allure.feature('Calculator')
@allure.story('Substraction')
@pytest.mark.smoke
@pytest.mark.parametrize('x,y,expected',[
    (0,0,0),
    (1,0,1),
    (0,1,-1),
    (1,1,0),
    (2,1,1),
    (1,2,-1),
    (-1,-1,0),
    (-1,-2, 1),
    (-2,-1,-1)
])
def test_subtract_normal(x,y, expected):
    assert calc.subtract(x,y) == expected

@allure.feature('Calculator')
@allure.story('Substraction')
@pytest.mark.xfail
@pytest.mark.parametrize('x,y,expected',[
    (None, None, ValueError),
    (None,0, ValueError),
    (0, None, ValueError),
    (None,'0', ValueError),
    ('0', None, ValueError),
    ('1',0, ValueError) ,
    (10,'3', ValueError),
    ('-12', '-31', ValueError),

])
def test_subtract_fail(x,y, expected):
    assert calc.subtract(x,y) == expected
