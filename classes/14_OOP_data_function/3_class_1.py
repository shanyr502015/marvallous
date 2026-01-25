class demo:
    def __init__(self):
        print("inside constructor")
    
    def __del__(self): # call honee optional ahe, GC thread ahe periodically run hote, like housekeeping come at any time to collect your garbade outside house in society so gc in python implicite.
        print("inside destructor") 

obj = demo()
print("end of application")