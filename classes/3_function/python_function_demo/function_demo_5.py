# accept: one parameters
# return : nothing
def marvallous1(value): # function definition with one parameter.
    print("inside marvallou1 :", value) # function body, prints message with parameter.

def main(): # main function definition, program entry point.
    marvallous1("python") # function call with string argument.
    marvallous1(21)      # function call with integer argument.

if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.