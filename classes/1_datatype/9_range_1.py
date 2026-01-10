# Range datatype 
# range(start,stop,step)
    # default start=0, step=1
    # stop is required, stop is exclusive
    # step can be negative also
# immutable 
# ordered
# indexed   
# used in for loop, iteration, etc.
# memory efficient, generates values on demand (lazy evaluation)

data = range(7) # 0 to 6
print(data) # range(0, 7)
print(type(data)) # <class 'range'>
print("--"*20) 

test = range(3,9,2) # 3 to 8, step 2
print(test) # range(3, 9, 2)
print(type(test)) # <class 'range'>
print("--"*20)