import gc

class demo:
    def __init__(self):
        print("inside constructor")
    
    def __del__(self): # call honee optional ahe, GC thread ahe periodically run hote, like housekeeping come at any time to collect your garbade outside house in society so gc in python implicite. yenar guranteed but when can not tell.
        print("inside destructor") 

# three steps for better code writing-> allocate, use, deallocate

# allocate
obj = demo() # object laa memory allocate kele

# use

# deallocate
del obj

gc.collect() # its is request is GC to collect garbage, python support request not order, gc 

print("end of application")