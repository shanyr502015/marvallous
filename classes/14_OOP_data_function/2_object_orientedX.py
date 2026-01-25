class arithmatic:
    def addition(self,a,b):
        return a + b

    def subtraction(self,a,b):
        return a - b

no1 = 0
no2 = 0
ans = 0

no1 = int(input("enter fist number : "))
no2 = int(input("enter second number : "))

obj = arithmatic()  

# ans = arithmatic().addition(no1,no2)
ans = obj.addition(no1,no2)
print("addition is :", ans)

# ans = arithmatic().subtraction(no1,no2)
ans = obj.subtraction(no1,no2)
print("subtraction is :", ans)