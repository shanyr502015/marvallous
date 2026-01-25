import gc

class demo:
    # class variable
    no1 = 10
    no2 = 11

    def __init__(self):
        # instance variable
        self.a = 101
        self.b = 201
        print("inside constructor")
    
    def __del__(self): 
        print("inside destructor") 

print(demo.no1)
print(demo.no2)

# print(demo.a) # attribute error
# print(demo.b) # attribute error

# beed to creadte object to call attribute error will gone

obj = demo()
print(obj.a)
print(obj.b)
