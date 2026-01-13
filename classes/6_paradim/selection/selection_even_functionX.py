# procedural
def checkeven(no):
    if (no % 2 == 0):
        print("it is even")
    else:
        print("it is odd")

def main():
    value = 0

    print("enter number: ")
    value = int(input())

    checkeven(value)
    
if __name__ == "__main__":
    main()