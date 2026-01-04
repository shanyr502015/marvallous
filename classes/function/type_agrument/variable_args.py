def addition(*no):
    print(no)
    print(type(no)) # tupless
    print(len(no))

def main():
    # addition(11,21)
    # addition(11,21,51,110)
    addition(11,11,21,51,110) # duplicate allowed in tuples


if __name__ == '__main__':
    main()