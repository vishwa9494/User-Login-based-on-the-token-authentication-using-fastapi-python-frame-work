from app.calculation import add,substract,multiply,divide
import pytest

@pytest.mark.parametrize("num1,num2,expected",[
    (3,2,5),
    (7,1,8),
    (12,4,16)        
])
def test_add(num1,num2,expected):
    print("testing add function")
    
    assert add(num1,num2)==expected


def test_substract(num1,num2,expected):
    assert substract(num1,num2)==expected


def test_multiply(num1,num2,expected):
    assert multiply(num1,num2)==expected

def test_divide(num1,num2,expected):
    assert divide(num1,num2)==expected






