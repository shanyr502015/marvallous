class parent : # root no need ()
    def __init__(self) :
        print("inside parent constructor")
        self.no1 = 10
        self.no2 = 20

    def fun(self):
        print("inside fun method of parent")

class child(parent):
    def __init__(self):
        super().__init__() # super( it is method in python
        print("inside child constructor")
        self.a = 11
        self.b = 21

    def sun(self):
        print("inside sun method of child")

cobj = child() # allocate memory to child