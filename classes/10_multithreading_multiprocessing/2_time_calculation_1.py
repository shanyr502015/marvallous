def factorial(no):
    fact = 1

    for i in range(1, no+1):
        fact = fact * i
    return fact

def main():

    value = int(input("enter number:"))

    ret = factorial(value)

    print("factorial is :", ret)


if __name__ == "__main__":
    main()

# enter number = 5000, bubble broke