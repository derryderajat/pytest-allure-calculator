import math

class Calculator:
    def __init__(self) -> None:
        pass
    
    def add(self, value1, value2):
        if not (isinstance(value1, int) and isinstance(value2, int)):
            raise ValueError("Both arguments must be integers")
        return value1 + value2

    def subtract(self, value1, value2):
        if not (isinstance(value1, int) and isinstance(value2, int)):
            raise ValueError("Both arguments must be integers")
        return value1 - value2

    def multiply(self, value1, value2):
        if not (isinstance(value1, int) and isinstance(value2, int)):
            raise ValueError("Both arguments must be integers")
        return value1 * value2

    def divide(self, value1, value2):
        if not (isinstance(value1, int) and isinstance(value2, int)):
            raise ValueError("Both arguments must be integers")
        if value2 == 0:
            raise ValueError("The divisor (value2) cannot be zero")
        return value1 / value2
    
    def exponentiate(self, base, exponent):
        if not (isinstance(base, int) and isinstance(exponent, int)):
            raise ValueError("Both arguments must be integers")
        return base ** exponent

    def root(self, value, degree=2):
        if not (isinstance(value, int) and isinstance(degree, int)):
            raise ValueError("Both arguments must be integers")
        if value < 0:
            raise ValueError("The value must be non-negative")
        return value ** (1 / degree)
    
    def absolute(self, value):
        if not isinstance(value, int):
            raise ValueError("The argument must be an integer")
        return abs(value)
