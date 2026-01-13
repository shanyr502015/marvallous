def main():
    size = 0
    value = 0

    print("enter number of elements :")
    size = int(input())

    data = list()

    print("enter the element :")

    for i in range(size):
        value = int(input())
        data.append(value) # siliar to C++, C, JAVA ---> data[i] = value
    
    # print(data)
    sum = 0
    
    for i in range(size):
        sum = sum + data[i]
    print("summation is :", sum)

if __name__ == "__main__":
    main()