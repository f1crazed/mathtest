import itertools, random
from enum import Enum

class MathOperator(Enum):
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4

class MathEquation:
    num1:int
    num2:int
    answer:int
    equation_type:MathOperator
    def __init__(self, num1:int, num2:int, equation_type:MathOperator):
        self.num1=num1
        self.num2=num2
        self.equation_type = equation_type
    def write_numbers(self):
        return f"{self.equation_type.name}{self.num1}{self.num2}{self.answer}"
    def compute_equation(self):
        if self.equation_type == MathOperator.ADDITION:
            self.answer = self.num1 + self.num2
        elif self.equation_type == MathOperator.SUBTRACTION:
            self.answer = self.num1 - self.num2
        elif self.equation_type == MathOperator.MULTIPLICATION:
            self.answer = self.num1 * self.num2
        elif self.equation_type == MathOperator.DIVISION:
            self.answer = self.num1 / self.num2
        else:
            raise Exception("Oporater not selected.")
        
        