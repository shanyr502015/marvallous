import os

def main ():
    filename = input("enter the name of file :")
    if (os.path.exists(filename)):
        fobj = open(filename,"r")
        print(fobj.name) # demo.txt
        print(fobj.mode) # r
        print(fobj.closed) # false
        fobj.close()
        print(fobj.closed) # true
    else:
        print("there is no such file")

if __name__ == "__main__":
    main()