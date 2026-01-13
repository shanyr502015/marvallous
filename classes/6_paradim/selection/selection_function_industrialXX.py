# procedural

def checkeven(no):
    return (no % 2 == 0) # code reduction not optimization, for optimization iterations should get decrease

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