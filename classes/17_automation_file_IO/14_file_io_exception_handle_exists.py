import os

def main ():
    filename = input("enter the name of file :")

    ret = os.path.exists(filename)

    if (ret == True):
        fobj = open(filename,"r")
        print("file gets successfully open")
        
    else:
        print("there is no such file")

    


if __name__ == "__main__":
    main()