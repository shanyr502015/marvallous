########################################################## function_1.py ############################################################
# method/api/rest api all are functions (function block of code which only runs when it is called)
# static way taking input & processing
no1 = 10
no2 = 11
ans = no1 * no2 # this is business logic of programm (here multiplication business operation)
print("multiplication is :", ans)

########################################################## function_2.py ##########################################################
# dynamic way of taking input and processing
print("enter first number : ") # prompt message to user
no1 = input() # 10, input() function takes input in string format, so no1 will be string '10', not integer 10.
print("enter second number : ") # prompt message to user
no2 = input() # 11, input() function takes input in string format, so no2 will be string '11', not integer 11.

ans = no1 + no2 # TypeError: can't multiply sequence by non-int of type 'str', because input() function always takes input in string format
print("multiplication is :", ans)

########################################################## function_3.py ##########################################################
# dynamic way of taking input & processing with type conversion
print("enter first number : ")
no1 = int(input()) # 10, converting string input to integer_type, so no1 will be integer 10.
print("enter second number : ")
no2 = int(input()) # 11, converting string input to integer_type, so no2 will be integer 11.

ans = no1 * no2 # 110, now multiplication will work fine because we converted input string to integer_type.
print("multiplication is :", ans) # 110 (correct multiplication because we converted input string to integer_type)

########################################################## function_4.py ##########################################################
# repetitive way of taking input and processing (not following DRY principle)
print("enter first number : ")
no1 = int(input())
print("enter second number : ")
no2 = int(input())

ans = no1 * no2
print("multiplication is :", ans)
print("--"*15)
# -------------------------------
print("enter first number : ")
no1 = int(input())
print("enter second number : ")
no2 = int(input())

ans = no1 * no2
print("multiplication is :", ans)
print("--"*15)
# ---------------------------------
print("enter first number : ")
no1 = int(input())
print("enter second number : ")
no2 = int(input())

ans = no1 * no2
print("multiplication is :", ans)
print("--"*15)
##########################################################################################################################################################
# Note: Above code is repetitive, we are repeating same code block multiple times. This is against DRY principle (Do Not Repeat Yourself principle) of programming.
# To follow DRY principle, we should use functions to encapsulate the repetitive code block and call it whenever needed.
# This way, we avoid code duplication and make our code more maintainable and reusable. 
# Next, we will see how to implement this using user-defined functions (UDF).   
##########################################################################################################################################################
def multiplication(value1,value2): # not self executable module (line with 0 indentation), defining function name as multiplication and arguments value1,value2 
    # The colon (:) after function definition line is mandatory in Python. It indicates start of function body, and all statements within function must be indented to form block under this definition.  
    # function body, all statements inside function body should be indented.
    ans = 0 # local variable declaration/initialization/definition/assignment/creation, local to this function only, not accessible outside this function.  
    ans = value1 * value2 # local variable declaration/initialization/definition/assignment/creation
    return ans # returning ans value to calling place, where function is called, return statement is always the last statement of function body.
# no1 = 0 , no2 = 0 , result = 0  # syntaxerror , see it imp
no1 = 0 # global varaible value assigned, ( supposer its item1 in shop) 
no2 = 0 # global varaible value assigned, ( supposer its item2 in shop)
result = 0 # global varaible (supposer its customer bag who went shop and bought some items in it by calling Ganeshshop function))
########## you went first time in shop #################
no1 = int(input("enter first number : ")) # taking input from user
no2 = int(input("enter first number : ")) # taking input from user

result = multiplication(no1, no2) # calling multiplication function by passing no1 and no2 as arguments, and returning value is stored in result variable.
print("multiplication is : ",result) # printing result variable value

#### you went second time in shop this is DRY ######
no1 = int(input("enter first number : "))
no2 = int(input("enter first number : "))

result = multiplication(no1, no2)
print("multiplication is : ",result)
# Now DRY (do not repeat yourself) principle is followed here by using function multiple times, so no code repetition.
####################################################################################################################
