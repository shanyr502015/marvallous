import gc

class demo:
    def __init__(self):
        print("inside constructor")
    
    def __del__(self): 
        print("inside destructor") 


obj1 = demo()

obj2 = demo()

del obj1
del obj2

gc.collect() 

print("end of application")