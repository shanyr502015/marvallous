def main ():
    try:
        open("demo.txt","r") # Explicit: You are telling Python "open this specifically for reading."
        print("file gets successfully open")

    except FileNotFoundError:
        print("unable to open file as there is no such file")


    finally:
        print("end of application")

if __name__ == "__main__":
    main()