def multiplication(value1,value2):
    ans = 0 # local variable
    ans = value1 * value2 # local variable
    return ans


# no1 = 0 , no2 = 0 , result = 0  # syntaxerror , see it imp
no1 = 0 
no2 = 0 
result = 0
########## you went first time in shop #################
no1 = int(input("enter first number : "))
no2 = int(input("enter first number : "))

result = multiplication(no1, no2)
print("multiplication is : ",result)
############# you went second time in shop ############ this is DRY
no1 = int(input("enter first number : "))
no2 = int(input("enter first number : "))

result = multiplication(no1, no2)
print("multiplication is : ",result)