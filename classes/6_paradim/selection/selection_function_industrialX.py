# procedural

def checkeven(no):
    if (no % 2 == 0):
        return True
    else:
        return False

def main():
    value = 0
    ret = False # indirectly 0 (zero)

    print("enter number: ")
    value = int(input())

    ret = checkeven(value)
    
    if (ret == True):
        print("it is even")
    else:
        print("it is odd")
    
if __name__ == "__main__":
    main()