import os

def main ():
    filename = input("enter the name of file :")
    if (os.path.exists(filename)):
        os.remove(filename)
        print("file gets deleted")
    else:
        print("there is no file")

if __name__ == "__main__":
    main()