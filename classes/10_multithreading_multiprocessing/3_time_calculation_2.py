import time

def factorial(no):
    fact = 1

    for i in range(1, no+1):
        fact = fact * i
    return fact

def main():

    value = int(input("enter number:"))

    start_time = time.time()

    ret = factorial(value)
    
    end_time = time.time()

    print("factorial is :", ret)
    print("total execution time is:",end_time-start_time)

if __name__ == "__main__":
    main()

# enter number = 5000, bubble broke or milk outside utinsil