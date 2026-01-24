def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

no1 = 0
no2 = 0
ans = 0

no1 = int(input("enter fist number : "))
no2 = int(input("enter second number : "))

ans = addition(no1, no2)
print("addition is :", ans)

ans = subtraction(no1, no2)
print("subtraction is :", ans)