from mv_fmr_module import filterX, mapX, reduceX 

checkeven = lambda no : (no % 2 == 0)
increment = lambda no : no + 1
add = lambda a,b: a + b

def main():
    data = [11,10,15,20,22,27,30]
    print ("actual data :", data)

    fdata = list(filterX(checkeven, data)) 
    print("data after filer is :", fdata)

    mdata = list(mapX(increment,fdata))
    print("data after map is :",mdata)

    rdata = reduceX(add, mdata) 
    print("data after reduce is :",rdata)

if __name__ == "__main__":
    main()