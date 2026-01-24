addition = lambda a,b: a + b  # lambda laa circular bracket nahi chalat, return keyword lambda laa chalat nahi

subtraction = lambda a,b: a - b

no1 = 0
no2 = 0
ans = 0

no1 = int(input("enter fist number : ")) # 11
no2 = int(input("enter second number : ")) # 10

ans = addition(no1, no2) # ans = no1 + no2 -> ans = 11 + 10, from this control not wnet to 1 line , instead body of 1 line come here , home delivery for lambda funciton
print("addition is :", ans) 

ans = subtraction(no1, no2) # ans = no1 - no2 ->  ans = 11 - 10
print("subtraction is :", ans)