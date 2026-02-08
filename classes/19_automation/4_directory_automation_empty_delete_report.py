import sys
import os

def directoryscanner(dirname = "mv"): 
    ret = False
    ret = os.path.exists(dirname)
    if (ret == False):
        print("there is no such dir")
        return
    
    ret = os.path.isdir(dirname)
    if ret == False :
        print("id is not dir")
        return
    
    filecount = 0
    emptyfilecount = 0

    for foldername, subfolder, filename in os.walk(dirname):
        
        for fname in filename:
            filecount = filecount + 1

            fname = os.path.join(foldername,fname)
            print("file name :",fname)
            print ("file size :",os.path.getsize(fname))

            if (os.path.getsize(fname) == 0):
                emptyfilecount = emptyfilecount + 1
                os.remove(fname)

    border = "_"*50
    print(border)
    print("---------------automation report ------------------")
    print("total files scanned :", filecount)
    print("total empty files found :", emptyfilecount)
    print(border)


def main():
    border = "_"*50
    print(border)
    print("----------------mv dir automation-----------------")
    print(border)

    if (len(sys.argv) != 2):
        print("invalid number fo arguments")
        print("please specify name of dir")
        return

    directoryscanner(sys.argv[1])
    border = "_"*50
    print(border)
    print("----------------mv dir automation-----------------")
    print(border)

if __name__ == "__main__":
    main()




