num1 = int(input("Enter first number: ")) # 3
num2 = int(input("Enter second number: ")) #2

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

print(f"Addition: {addition}") #5
print(f"Subtraction: {subtraction}") #1
print(f"Multiplication: {multiplication}") #6
print(f"Division: {division}") #1.5
