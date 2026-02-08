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

def directorywatcher(directoryname = "mv"):
    ret = False
    ret = os.path.exists(directoryname)

    if ret == False:
        print("there is no such directoy")
        return
    
    ret = os.path.isdir(directoryname)

    if ret ==  False :
        print("it is not dir")
        return
    
    for foldername, subfoldername, filename in os.walk(directoryname):
        for fname in filename:
            fname = os.path.join(foldername,fname)
            checksum = calculatechecksum(fname)

            print(f"file name  is : {fname} --and-- checksum is : {checksum}")

def main():
    directorywatcher()



if __name__ == "__main__":
    main()