from src.calculator import Calculator
import pytest
import allure
calc = Calculator()
test_data = []

@pytest.mark.smoke
@pytest.mark.regression
def test_add_positive_number():
    assert calc.add(1,2)==3

@allure.feature('Calculator')
@allure.story('Addition')    
@pytest.mark.smoke
@pytest.mark.parametrize("a,b,expected",[
    (0,0,0),
    (0,1,1),
    (1,0,1),
    (-1,0,-1),
    (0,-1,-1),
    (-1,-1,-2),
])
def test_add_normal(a,b,expected):
    assert calc.add(a,b) == expected
@allure.feature('Calculator')
@allure.story('Addition')
@pytest.mark.smoke
@pytest.mark.xfail
@pytest.mark.parametrize("a,b,expected_raise",[
    (0,"1",TypeError),
    ("1",1,TypeError),
    ("10","10",TypeError),
    (None,10,TypeError),
    (20,None, TypeError),
    ("20",None,TypeError),
    (None,"20", TypeError),
    (None, None, TypeError),
])
def test_add_fail(a,b, expected_raise):
    with pytest.raises(expected_raise):
        calc.add(a,b)