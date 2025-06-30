class Calculator:
    def calculate(self, a, b, operation):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            return a / b if b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Operation (add, subtract, multiply, divide): ")
calc = Calculator()
print("Result:", calc.calculate(a, b, op))
