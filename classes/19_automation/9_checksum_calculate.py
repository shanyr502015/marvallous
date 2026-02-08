import hashlib

def calculatechecksum(filename):
    fobj = open(filename,"rb")
    hobj = hashlib.md5()
    print("calculating checksum for file :",filename)
    buffer = fobj.read(1000)
    print("buffer size is :",len(buffer))

    while (len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1000)
    fobj.close()
    return hobj.hexdigest()

def main():
    ret = calculatechecksum("demo.txt")
    print("checksum is :", ret)


if __name__ == "__main__":
    main()