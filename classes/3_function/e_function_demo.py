#####################################################################################################################################################
def main(): # Define main function, serves as entry point of program, when executed directly.
    print("inside main") # Print a message indicating we are inside main function.

if __name__ == "__main__": # Check if this script is being run directly (not imported as a module).  
    main() # If so, call main function to execute code within it.   
#####################################################################################################################################################
# empty fucntion
def main(): 
    pass # placeholder for future code, does nothing, avoids syntax errors.
    

if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.
#####################################################################################################################################################
# not good programming practice
def main():
    print("inside main")
    pass
    
    
if __name__ == "__main__": 
    main()
#####################################################################################################################################################
# accept: nothing
# return : nothing
def marvallous1(): # function definition, no parameters, no return.
    print("inside marvallou1") # function body, prints message.

def main(): # main function definition, program entry point.
    marvallous1() # function call, invokes marvallous1, no arguments.
    
if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.
#####################################################################################################################################################
# accept: one parameters
# return : nothing
def marvallous1(value): # function definition with one parameter.
    print("inside marvallou1 :", value) # function body, prints message with parameter.

def main(): # main function definition, program entry point.
    marvallous1("python") # function call with string argument.
    marvallous1(21)      # function call with integer argument.

if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.
#####################################################################################################################################################
# accept: multiples parameters
# return : nothing
def marvallous1(value1, value2): # function definition with two parameters.
    print("inside marvallou1 :", value1, value2) # function body, prints message with parameters.

def main(): # main function definition, program entry point.
    marvallous1("python", 21) # function call with two arguments, string and integer.

if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.
#####################################################################################################################################################
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
#####################################################################################################################################################
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
#####################################################################################################################################################
# one fucntion can call another function
# use return keyword if want to return value oterwise no need

def fun(): # first function,zero parameter,no return
    print("inside fun")

def gun(): # second function,zero parameter,no return
    print("inside gun")

def main(): # main function,program entry point
    fun() # call first function
    gun() # call second function
    
if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.
#####################################################################################################################################################
# one fucntion can call another function

def fun():
    print("inside fun")

def gun():
    print("inside gun")
    gun()

def main():
    fun()


if __name__ == "__main__": 
    main()
#####################################################################################################################################################
# nested funciton only in  python
def phoenix(): 
    print("inside phoenix")
    def zara():
        print("inside zara")

def main():
    phoenix()

if __name__ == "__main__": 
    main()
#####################################################################################################################################################
# nested funciton only in  python
def phoenix(): 
    print("inside phoenix")
    def zara():
        print("inside zara")

# def main():
#     zara() # nameerror: name "zara" not defined

def main():
    phoenix.zara() # attributeerror: 'funciton' object has no attribute "zara"
   
if __name__ == "__main__": 
    main()
#####################################################################################################################################################
# nested funciton only in  python
def phoenix(): # outer function, zero parameter,no return type.
    print("inside phoenix")

    def zara(): # nested function, zero parameter,no return type.
        print("inside zara")
        # zara() # recursive fucntion
    zara() # nested fucniton, called inside outer function.

def main(): # main function, program entry point
    phoenix() # call outer function, which in turn calls nested function.
   

if __name__ == "__main__": # Check if the script is run directly ,not imported.
    main() # If true, execute main function.

# funciton can return anoter fuction we can see latter.
#####################################################################################################################################################