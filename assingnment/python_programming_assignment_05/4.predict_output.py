ba = bytearray([65, 66, 67])
ba[0] = 97
print(ba) # bytearray(b'aBC')
print(type(ba)) # <class 'bytearray'>

# Why is this allowed? 
    # bytearray is mutable (changeable).
    # So we can update its elements using indexing like ba[0] = ....
    # Here:
        # 65 = A
        # changed first element to 97 = a
    # So ABC becomes aBC.