# print(): shows output on screen, Used only for display, It does not send value back to caller.
# return: Sends output back from function to where it was called, Returned value can be stored in variable & used later, If no return, Python returns None.
def add_nums(a, b):
    print("Using print():", a + b)   #  Using print(): 30  (only displays output)
    return a + b                    # sends value back

result = add_nums(10, 20)
print("Stored result:", result)     #  Stored result: 30  (uses returned value)

# print() = display only
# return = give value back to use later