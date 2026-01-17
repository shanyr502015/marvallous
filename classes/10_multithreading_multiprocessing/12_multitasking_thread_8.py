import threading 

def sumeven(no):
    sum = 0
    for i in range(2, no+1 ,2):
        sum = sum + i
    print("enen sum is :", sum)

    
def main():
    print(sumeven(10))


if __name__ == "__main__":
    main()