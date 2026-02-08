def main ():
    try:
        open("demo.txt") # second parameter "r" default, Implicit: Python fills in the 'r' for you.
        print("file gets successfully open")

    except FileNotFoundError:
        print("unable to open file as there is no such file")


    finally:
        print("end of application")

if __name__ == "__main__":
    main()