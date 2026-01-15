# accept: multiples parameters
# return : one value
def marvallous1(value1, value2): # function definition with two parameters.
    print("inside marvallou1 :", value1, value2) # function body, prints message with parameters.
    return 11 # returns integer value 11    

def main():
    result = None # initialize result variable.
    result = marvallous1("python", 21) # function call with two arguments.
    print("return value inside main :", result) # print returned value.

if __name__ == "__main__":  # Check if the script is run directly ,not imported.
    main() # If true, execute main function.