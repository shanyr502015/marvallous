########################################################## function_1.py ############################################################
# static way of taking input and processing
no1 = 10
no2 = 11
ans = no1 * no2 # this is business logic of programm (here we want multiplication business operation)
print("multiplication is :", ans)

########################################################## function_2.py ##########################################################
# dynamic way of taking input and processing
print("enter first number : ")
no1 = input() # 10
print("enter second number : ")
no2 = input() # 11

ans = no1 * no2 # TypeError: can't multiply sequence by non-int of type 'str', because input() function always takes input in string format
print("multiplication is :", ans)

########################################################## function_3.py ##########################################################
# dynamic way of taking input and processing with type conversion
print("enter first number : ")
no1 = int(input()) # 10, converting string input to integer_type
print("enter second number : ")
no2 = int(input()) # 11, converting string input to integer_type

ans = no1 * no2
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