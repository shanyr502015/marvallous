def checkeven(no):
    return (no % 2 == 0)

def increment(no):
    return no + 1

def main():
    data = [11,10,15,20,22,27,30]
    print ("actual data :", data)

    
    fdata = list(filter(checkeven, data)) 
    print("data after filer is :", fdata)

    # mdata = map(increment,fdata)
    mdata = list(map(increment,fdata))
    print("data after map is :",mdata)

if __name__ == "__main__":
    main()
