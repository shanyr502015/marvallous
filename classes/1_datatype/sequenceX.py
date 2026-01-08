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
# value3[2] = 35, can not write since not support index, but mutabl we can see later