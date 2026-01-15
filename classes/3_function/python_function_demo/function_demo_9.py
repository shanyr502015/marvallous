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