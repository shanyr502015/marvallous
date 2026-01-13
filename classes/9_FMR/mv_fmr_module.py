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
# add = lambda a,b: a + b
def reduceX(task, elements):
    sum = 0
    # result = 0
    for no in elements:
        sum = task(sum,no)
    return sum