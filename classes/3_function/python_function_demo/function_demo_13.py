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