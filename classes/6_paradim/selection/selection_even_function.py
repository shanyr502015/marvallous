def checkeven(no):
    if (no % 2 == 0):
        print("it is even")
    else:
        print("it is odd")

def main():
    checkeven(21)      # positinal
    checkeven(no = 22) # keyword
    
if __name__ == "__main__":
    main()

#  user interaction should me inside main