def main():
    try:
        ans = 0
        print("enter first number:")
        no1 = int(input())
        print("enter second number:")
        no2 = int (input())
        print("inside try")
        ans = no1 / no2

    except ZeroDivisionError as zobj:
        print("inside except:",zobj)

    except ValueError as vobj:
        print("inside except:",vobj)

    except Exception as eboj:
        print("inside except :", eboj)
        

    finally:
        print("inside finally")
        


    print("division is :", ans)


if __name__ == "__main__":
    main()

# number / 0 --> not allowed in cpu(lu)