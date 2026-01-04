def multiplication(value1,value2): # shop
    ans = 0 # local variable
    ans = value1 * value2 # local variable
    return ans # return to caller, returning ans.   

def main(): # home
    no1 = 0 # variable declaration/initialization/definition/assignment/creation
    no2 = 0 # variable declaration/initialization/definition/assignment/creation
    result = 0 # variable declaration/initialization/definition/assignment/creation

    no1 = int(input("enter first number : ")) # taking input from user, converting string to integer, assigning to no1.
    no2 = int(input("enter first number : ")) # taking input from user, converting string to integer, assigning to no2.

    result = multiplication(no1, no2) # function call, passing no1 and no2 as arguments, storing return value in result.
    print("multiplication is : ", result) # printing the result to console.

main() # starter

############################ d_main.py ############################
def multiplication(value1,value2): # shop, not self executable module, line with 0 indentation, function definition.
    ans = 0 # local variable
    ans = value1 * value2 # local variable
    return ans # return to caller, returning ans.

def main(): # home, main function, not self executable module, line with 0 indentation, function definition.
    no1 = 0 # variable declaration/initialization/definition/assignment/creation    
    no2 = 0 # variable declaration/initialization/definition/assignment/creation
    result = 0 # variable declaration/initialization/definition/assignment/creation

    no1 = int(input("enter first number : ")) # taking input from user, converting string to integer, assigning to no1.
    no2 = int(input("enter first number : ")) # taking input from user, converting string to integer, assigning to no2.

    result = multiplication(no1, no2) # function call, passing no1 and no2 as arguments, storing return value in result.
    print("multiplication is : ",result) # printing the result to console.

# starter
if __name__=="__main__": # check if script is run directly, not imported as module.     
    main() # calling main function to start execution.
#####################################################################