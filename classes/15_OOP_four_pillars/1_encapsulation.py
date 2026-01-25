class arithematic :
    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b
        print("object gets created successfully")
    
    def addition(self):
        ans = 0
        ans = self.no1 + self.no2
        return ans 
    
    def substraction(self):
        ans = 0
        ans = self.no1 - self.no2
        return ans 


obj1 = arithematic(11,10) # arithmatic(id(obj1),11,10) --> __init__(id(obj1),11,10)
obj2 = arithematic(21,20) # arithmatic(id(obj2),21,20) --> __init__(id(obj2),21,20)

ret = obj1.addition() # addition(id(obj1))  --> addition(1000)
print(ret) # 21

ret = obj2.substraction() # substraction(id(obj2))  --> substraction(2000)
print(ret) # 1