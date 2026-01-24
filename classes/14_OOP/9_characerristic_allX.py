class demo:
    no = 10
    
    def __init__(self,a,b):
        self.value1 = a
        self.value2 = b

print("class variable no :", demo.no)

obj1 = demo(11,21) # your plate
obj2 = demo(51,101) # my plate

# print(obj1.no) # class and object by both we can call - class variable , allowed but good with class

print("instance variable of obj1 :", obj1.value1,obj1.value2) # 11, 21
print("instance variable of obj2 :", obj2.value1,obj2.value2) # 51, 101

obj1.value1 = 15 # 11 change to 15

demo.no = 0 # 10 change to 0

print("instance variable of obj1 :", obj1.value1,obj1.value2) # 15, 21
print("instance variable of obj2 :", obj2.value1,obj2.value2) # 51, 101

print(obj1.no) # 0
print(obj2.no) # 0

# this is after python 2.6 version which nullify out common onion,pickle,lemon so good practice to class variable using class not by object
# obj1.no = 0
# print(obj1.no) # 0
# print(obj2.no) # 10