# Function with parameters: function that receives values from user or program, these values are called parameters.
def add_nums(a, b):
    return a + b

result = add_nums(10, 20)
print(result) # 30
# explaination:a & b are parameters --> Values 10 and 20 are passed to function --> Function uses them to produce output

# Function without parameters: A function that does not receive any values from user or program, all data is defined inside the function
def Hello():
    print("Hello, Shantaram!")

Hello() # Hello, Shantaram!
# explaination: No parameters are passed, Function runs using its own internal code