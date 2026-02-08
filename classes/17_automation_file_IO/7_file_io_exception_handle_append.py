def main ():

    
    try:
        fobj = open("hello.txt","a")
        print("file gets successfully open")

        fobj.write("python automation...") # by default mode to write is text
        fobj.close()

    except FileNotFoundError:
        print("unable to open file as there is no such file")


    finally:
        print("end of application")
        

if __name__ == "__main__":
    main()