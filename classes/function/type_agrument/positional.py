def display(a,b,c,d):
    print(a,b,c,d)

def main():
    # display(10,20) # not allowed-les agruments # typeerror: display() misssing 2 required positional agrument 'c' and 'd'
    # display(10,20,30,40,50) # not allowed-extra agrguments # typeerror: display() take 4 positional garuments but 5 were given
    display(10,20,30,40) # allowed

if __name__ == '__main__':
    main()