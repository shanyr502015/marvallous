class parent : # root no need ()
    def __init__(self) :
        print("inside parent constructor")
        self.no1 = 10
        self.no2 = 20

    def fun(self):
        print("inside fun method of parent",self.no1,self.no2)

class child(parent):
    def __init__(self):
        super().__init__() # super( it is method in python
        print("inside child constructor")
        self.a = 11
        self.b = 21

    def sun(self):
        print("inside sun method of child",self.a,self.b,self.no1,self.no2)

cobj = child() # allocate memory to child

print(cobj.no1) # 10, naked call
print(cobj.no2) # 20, naked call

print(cobj.a) # 11, naked call
print(cobj.b) # 21, naked call


cobj.fun()
cobj.sun()