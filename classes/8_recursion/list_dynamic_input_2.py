def main():
    size = 0
    print("enter elements :")
    size = int(input())


    data = list()

    print("enter element :")

    for i in range(size):
        value = int(input())
        data.append(value)
    
    
    print(data)


if __name__ == "__main__":
    main()