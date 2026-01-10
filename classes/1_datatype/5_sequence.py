value1 = [10,20,30,40,10]
print(value1)
print(type(value1))

value2 = (10,20,30,40,10)
print(value2)
print(type(value2))

value3 = {10,20,30,40,10}
print(value3)
print(type(value3))


####### sequenceX ########
##################
# list, duplicate
value1 = [10,20,30,40,10] 
print(value1[0])  # print value1 of 0 , [] = of  , 10
value1[2] = 35


# tuple, duplicate
value2 = (10,20,30,40,10) 
print(value2[0])  # 10
# value2[2] = 35 # error

# set, no dujplicate
value3 = {10,20,30,40,10} 
# print(value3[0]) # error  ( not subscriptable - means not support index)
# value3[2] = 35, can not write since not support index, but mutable.

# Even though:
    # ❌ You cannot change elements using index
    # ✅ You can add or remove elements
    # So set is mutable, but unordered.

# Add a new element (allowed)
value3.add(35)
print(value3) # {35, 40, 10, 20, 30}
print(type(value3)) # set

#Remove an element (allowed)
value3.remove(20)
print(value3) # {35, 40, 10, 30}
print(type(value3)) # set

#Try index access (NOT allowed)
# print(value3[0]) # error  ( not subscriptable - means not support index)

###################

# revision of sequence ########
################### sequence

arr = [10,20,30,40,10]
print(arr)
print(type(arr))
print("-"*40)

brr = (10,20,30,40,10)
print(brr)
print(type(brr))
print("-"*40)