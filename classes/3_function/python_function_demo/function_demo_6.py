# accept: multiples parameters
# return : nothing
def marvallous1(value1, value2): # function definition with two parameters.
    print("inside marvallou1 :", value1, value2) # function body, prints message with parameters.

def main(): # main function definition, program entry point.
    marvallous1("python", 21) # function call with two arguments, string and integer.

if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.