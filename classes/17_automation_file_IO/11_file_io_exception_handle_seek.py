# offset - presently where you are - use of tell() method
def main ():
    
    try:
        fobj = open("hello.txt","r")
        print("file gets successfully open")
        print("current offset is :",fobj.tell()) # 0

        fobj.seek(7)
        print("current offset is :",fobj.tell()) # 7

        data = fobj.read(10)

        print("current offset is :",fobj.tell()) # 17

        print("data from file is:",data)
        fobj.close()

    except FileNotFoundError:
        print("unable to open file as there is no such file")


    finally:
        print("end of application")

if __name__ == "__main__":
    main()