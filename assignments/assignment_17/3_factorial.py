# Write a program which accept one number from user and return its factorial.
# Input : 5                        Output : 120

def factorial(num):
    fact = 1
    for i in range(1,num + 1):
        fact = fact * i
    return fact

def main():
    num = int(input("enter number here : "))
    ret = factorial(num)
    print (f"factorial of {num} is : {ret}")

if __name__ == "__main__":
    main()