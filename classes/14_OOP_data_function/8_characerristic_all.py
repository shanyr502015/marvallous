class demo:
    no = 10
    
    def __init__(self,a,b):
        self.value1 = a
        self.value2 = b

print("class variable no :", demo.no)

obj1 = demo(11,21) # your plate
obj2 = demo(51,101) # my plate

print("instance variable of obj1 :", obj1.value1,obj1.value2)
print("instance variable of obj2 :", obj2.value1,obj2.value2)