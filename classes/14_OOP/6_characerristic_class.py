import gc

class demo:
    # class variable
    no1 = 10
    no2 = 11

    def __init__(self):
        print("inside constructor")
    
    def __del__(self): 
        print("inside destructor") 

print(demo.no1)
print(demo.no2)