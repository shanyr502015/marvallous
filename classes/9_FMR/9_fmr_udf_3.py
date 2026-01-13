# from functools import reduce 

checkeven = lambda no : (no % 2 == 0)
increment = lambda no : no + 1
add = lambda a,b: a + b

def filterX(task, elements):
    result = list() # result = [] as well but keep that best practice
    for no in elements:
        ret = task(no)

        if (ret == True):
            result.append(no)

    return result

def mapX(task, elements):
    result = list()

    for no in elements:
        ret = task(no)
        result.append(ret)

    return result
# # add = lambda a,b: a + b
def reduceX(task, elements):
    sum = 0
    # result = 0
    for no in elements:
        sum = task(sum,no)
    return sum
# def reduceX(task, elements):
#     result = 0
#     for no in elements:
#         result = task(result, no)
#     return result


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