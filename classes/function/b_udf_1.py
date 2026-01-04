########################################################## function_3.py ##########################################################
# dynamic way of taking input and processing with type conversion
print("enter first number : ")
no1 = int(input()) # 10, converting string input to integer_type
print("enter second number : ")
no2 = int(input()) # 11, converting string input to integer_type

ans = no1 * no2
print("multiplication is :", ans) # 110 (correct multiplication because we converted input string to integer_type)

########################################################## udf_1.py ############################################################
# user defined function (UDF) for multiplication business logic to follow DRY principle(do not repeat yourself principle)
#  function name multiplication is generic and used multiple times in the same file
def multiplication(value1,value2): # function definition, defining function name as multiplication and parameters value1,value2 
    # The colon (:) after function definition line is mandatory in Python. It indicates start of function body, and all statements within function must be indented to form block under this definition.  
    # function body, all statements inside function body should be indented
    ans = 0 # local variable declaration/initialization/definition/assignment/creation
    ans = value1 * value2 # local variable declaration/initialization/definition/assignment/creation
    return ans # returning ans value to calling place, where function is called, return statement is always the last statement of function body.

print("demo application")

########################################################## udf_2.py ############################################################
def multiplication(value1,value2): # not self executable module (line with 0 indentation)
    ans = 0 
    ans = value1 * value2 
    return ans 

print("demo application") # self executable module (line with 0 indentation)

no1 = 10 # global varaible value assigned, ( supposer its item1 in shop)
no2 = 11 # global varaible value assigned, ( supposer its item2 in shop)
result = 0  # global varaible (supposer its customer bag who went shop and bought some items in it by calling Ganeshshop function))

result = multiplication(no1, no2) # calling multiplication function by passing no1 and no2 as arguments, and returning value is stored in result variable. (calls the function and stores return value in result variable, which is global variable)
print("multiplication is : ",result) # printing result variable value, which is global variable. (we need to show what we bring from ganeshshop in the bag to our mother at home)

# interpreter runs indentation 0 lines top-to-bottom, 
# BUT ❌ wrong to say first executed line "print("demo application")" because function definition line "def multiplication(value1,value2): " is also indentation 0 line, but its not self executable line.
# function definition line "def multiplication(value1,value2): " executes it in sense that it creates function object and stores it in memory.It just does not run function body until you call it.
# NOTE: only self executable lines with indentation 0 are executed top-to-bottom by interpreter.
# NOTE:
    # Python executes the file from top to bottom.
    # First it processes the function definition (creates the function, does NOT run its body).
    # Then it executes the next top-level statements like print(), variable assignments, and function calls.

########################################################## udf_3.py ############################################################
def multiplication(value1,value2):
    ans = 0 
    ans = value1 * value2 
    return ans

# no1 = 0 , no2 = 0 , result = 0  # syntaxerror , see it imp
no1 = 0 
no2 = 0 
result = 0

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
###############################################################################################################################
