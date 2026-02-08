import hashlib
import os

def calculatechecksum(filename):
    fobj = open(filename,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(1000)

    while (len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def findduplicate(directoryname = "mv"):
    ret = False
    ret = os.path.exists(directoryname)

    if ret == False:
        print("there is no such directoy")
        return
    
    ret = os.path.isdir(directoryname)

    if ret ==  False :
        print("it is not dir")
        return
    
    duplicate = {}

    for foldername, subfoldername, filename in os.walk(directoryname):
        for fname in filename:
            fname = os.path.join(foldername,fname)
            checksum = calculatechecksum(fname)

            if checksum in duplicate:
                duplicate[checksum].append(fname)
            else:
                duplicate[checksum] = [fname]

    return duplicate 

def displayresult(mydict):
    result = list(filter(lambda x : len(x)>1, mydict.values()))
    count = 0
    for value in result:
        for subvalue in value:
            count = count + 1
            print(subvalue)
        print("value of count is:",count)
        count = 0


def deleteduplicate(path = "mv"):
    mydict = findduplicate(path)

    result = list(filter(lambda x : len(x)>1, mydict.values()))
    count = 0
    cnt = 0
    for value in result:
        for subvalue in value:
            count = count + 1
            if count > 1 :
                print("deleted file :",subvalue)
                os.remove(subvalue)
                cnt = cnt + 1
        count = 0
     

def main():
    ret = findduplicate()
    displayresult(ret)


if __name__ == "__main__":
    main()