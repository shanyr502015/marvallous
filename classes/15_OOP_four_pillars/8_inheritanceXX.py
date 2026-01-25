# override, run time polymorphism, overloadding not in python
class parent :
    def __init__(self) :
        print("inside parent constructor")

    def fun(self):
        print("inside fun method of parent")

class child(parent):
    def __init__(self):
        super().__init__() 
        print("inside child constructor")

    def fun(self):
        super().fun()
        print("inside fun method of child")

cobj = child() 

cobj.fun()