# accept: multiples parameters
# return : multiple value (only in python allowed)
def marvallous1(value1, value2): # function definition with two parameters.
    print("inside marvallou1 :", value1, value2) # function body, prints message with parameters.
    return 11, 21, 51 # returns multiple integer values

def main():
    result1 = None # initialize result1 variable.
    result2 = None # initialize result2 variable.
    result3 = None # initialize result3 variable.

    result1, result2, result3 = marvallous1("python", 21) # function call with two arguments.
     # unpack returned multiple values into result1, result2, result3 variables.
    print("return value :", result1, result2, result3) 

if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.