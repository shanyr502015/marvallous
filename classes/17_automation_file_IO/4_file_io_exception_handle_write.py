def main ():
    try:
        open("hello.txt","w")
        print("file gets successfully open")

    except FileNotFoundError:
        print("unable to open file as there is no such file")


    finally:
        print("end of application")

if __name__ == "__main__":
    main()