from src.calculator import Calculator
import pytest
import allure
calc = Calculator()
def test_multiply():
    assert calc.multiply(1,4) == 4

@allure.feature('Calculator')
@allure.story('Multiply')
@pytest.mark.smoke
@pytest.mark.parametrize('x,y,expected',[
    (0,0,0),
    (4,0,0),
    (0,16,0),
    (13,2,26),
    (2,1,2),
    (0,2,0),
    (-10,0,0),
    (-10,-0, 0),
    (-20,-10,200)
])
def test_multiply_normal(x,y, expected):
    assert calc.multiply(x,y) == expected

@allure.feature('Calculator')
@allure.story('Multiply')
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
def test_multiply_fail(x,y, expected):
    assert calc.multiply(x,y) == expected
