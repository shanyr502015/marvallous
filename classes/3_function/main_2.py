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


if __name__ == "__main__": # starter
    main() 
