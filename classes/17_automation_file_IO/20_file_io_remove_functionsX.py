import os

def main ():
    filename = input("enter the name of file :")
    if (os.path.exists(filename)):
        # fobj = open(filename,"r")
        fobj = open(filename,"w")

        print(fobj.readable())
        print(fobj.writable())
        print(fobj.seekable())

    else:
        print("there is no such file")

if __name__ == "__main__":
    main()