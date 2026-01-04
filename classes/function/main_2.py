def multiplication(value1,value2): # shop
    ans = 0 # local variable
    ans = value1 * value2 # local variable
    return ans

def main(): # home
    no1 = 0 
    no2 = 0 
    result = 0

    no1 = int(input("enter first number : "))
    no2 = int(input("enter first number : "))

    result = multiplication(no1, no2)
    print("multiplication is : ",result)

# starter
if __name__=="__main__": # 18-19 19-6 7 8 9 11 12 14 15 14-1 2 3 4 14 15
    main() 

# 17 - 6 ,14 - 1, 1-4-14, 14-15-18