from functools import reduce 

checkeven = lambda no : (no % 2 == 0)
increment = lambda no : no + 1
add = lambda a,b: a + b

def main():
    data = [11,10,15,20,22,27,30]
    print ("actual data :", data)

    fdata = list(filter(checkeven, data)) 
    print("data after filer is :", fdata)

    mdata = list(map(increment,fdata))
    print("data after map is :",mdata)

    rdata = reduce(add, mdata) 
    print("data after reduce is :",rdata)

if __name__ == "__main__":
    main()

# loop then convert recursion