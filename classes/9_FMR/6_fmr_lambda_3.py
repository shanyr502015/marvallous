from functools import reduce 
# checkeven = 
# increment = 
# add = 
def main():
    data = [11,10,15,20,22,27,30]
    print ("actual data :", data)

    fdata = list(filter(lambda no : (no % 2 == 0), data)) 
    print("data after filer is :", fdata)

    mdata = list(map(lambda no : no + 1,fdata))
    print("data after map is :",mdata)

    rdata = reduce(lambda a,b: a + b, mdata) 
    print("data after reduce is :",rdata)

if __name__ == "__main__":
    main()
# loop then convert recursion