def fun():
    x = 10
    print(x) # 10

fun()
print(x) # NameError: name 'x' is not defined
# explaination: 
    # x is defined inside function fun(), so it's local variable exists inside that function. So print(x) inside fun() works fine.
    # But outside function, x does not exist, so print(x) gives NameError. 
    # This shows variables defined inside functions are local to those functions & cannot be accessed outside.
