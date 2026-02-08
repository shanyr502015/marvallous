import sys
import os

def directoryscanner(dirname = "mv"): 
    border = "_"*50

    fobj = open("mv logs","w")

    fobj.write(border+"\n")
    fobj.write("this is log file created by mv automation\n")
    fobj.write("this is dir cleaner report\n")

    ret = False
    ret = os.path.exists(dirname)
    if (ret == False):
        print("there is no such dir")
        fobj.write("there is no such dir\n")
        fobj.close()
        return
    
    ret = os.path.isdir(dirname)
    if ret == False :
        print("id is not dir")
        fobj.write("id is not dir\n")
        fobj.close()
        return

    filecount = 0
    emptyfilecount = 0

    for foldername, subfolder, filename in os.walk(dirname):
        
        for fname in filename:
            filecount = filecount + 1
            fname = os.path.join(foldername,fname)
            if (os.path.getsize(fname) == 0):
                emptyfilecount = emptyfilecount + 1
                os.remove(fname)

    fobj.write(border+"\n")
    fobj.write("total file scanned :"+str(filecount)+"\n")
    fobj.write("total empty file :"+str(emptyfilecount)+"\n")
    fobj.write(border+"\n")
    fobj.close()
    

    print("---------------automation report ------------------")
    print("tolal files scanned :", filecount)
    print("tolal empty files found :", emptyfilecount)
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