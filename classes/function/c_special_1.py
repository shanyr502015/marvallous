############################ special.py ############################
print(__name__) # special variable
# When this file is run directly, __name__ is set to "__main__"
# When this file is imported as a module, __name__ is set to "special"        

############################ specialX.py ############################
# Compare this snippet from specialX.py:        
if __name__ == "__main__": # Check if the script is run directly    
    print("self executable file") # If true, execute this block
else: # If script is imported as a module, execute this block.  
    print("module file") # Print message for module import, not direct execution.
#####################################################################