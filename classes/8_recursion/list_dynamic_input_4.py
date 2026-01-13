def summation(arr): # arr is nickname of data here
    sum = 0
    
    for i in range(len(arr)):
        sum = sum + arr[i]

    return sum

def main():
    size = 0
    value = 0
    ret = 0

    print("enter number of elements :")
    size = int(input())

    data = list() # dynamic meomory to list

    print("enter the element :")

    for i in range(size):
        value = int(input())
        data.append(value) 
    
    ret = summation(data)

    print("summation is :", ret)

if __name__ == "__main__":
    main()