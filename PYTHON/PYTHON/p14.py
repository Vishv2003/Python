class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

calc = Calculator()
print(calc.add(5, 3))       
print(calc.subtract(10, 4))  
print(calc.multiply(6, 7))   
print(calc.divide(20, 5))    
print(calc.divide(10, 0))    
