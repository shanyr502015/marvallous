from functools import reduce # inbuild module no need internet connection to intall anything

# def checkeven(no):
#     return (no % 2 == 0)

checkeven = lambda no : (no % 2 == 0)

# def increment(no):
#     return no + 1

increment = lambda no : no + 1

# def add(a,b):
#     return a + b

add = lambda a,b : a + b

def main():
    data = [11,10,15,20,22,27,30]
    print ("actual data :", data)

    
    fdata = list(filter(checkeven, data)) 
    print("data after filer is :", fdata)

    # mdata = map(increment,fdata)
    mdata = list(map(increment,fdata))
    print("data after map is :",mdata)

    rdata = reduce(add, mdata) # for reduce no need typecst as it will give only one value
    print("data after reduce is :",rdata)

if __name__ == "__main__":
    main()

# loop then convert recursion