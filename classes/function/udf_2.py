def multiplication(value1,value2):
    ans = 0 # local variable
    ans = value1 * value2
    return ans

print("demo application")

no1 = 10 # global varaible
no2 = 11 # global varaible
result = 0  # is result is bag also global varaible

result = multiplication(no1, no2)
print("multiplication is : ",result)

# indentation 0 and self executable , so fist excution here is ""print("demo application")""