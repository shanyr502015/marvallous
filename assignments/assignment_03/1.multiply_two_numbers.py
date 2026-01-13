# user-defined function: function created by user, used to perform specific task. User-defined function created using def keyword in python. 

def mul_num(a, b):
    return a * b

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

result = mul_num(num1, num2)
print(f"Multiplication: {result}")

# NOTE:
    # def mul_num(a, b): → defines user-defined function
    # return a * b → sends result back tocaller
    # Function is called using mul_num(num1, num2)