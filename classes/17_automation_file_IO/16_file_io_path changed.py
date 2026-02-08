import os

def main ():
    filename = input("enter the name of file :")

    ret = os.path.isabs(filename)

    if (ret == True):
        print("it is absolute path")
    else:
        print("it is relative  path")
        newpath = os.path.abspath(filename)
        print("updated path :",newpath)


if __name__ == "__main__":
    main()