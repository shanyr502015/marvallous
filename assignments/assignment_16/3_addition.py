# Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
# Input : 11   5            Output : 16

def Add(num1,num2):
    ans = num1 + num2
    return ans


def main():
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))

    ret = Add(num1,num2)
    print ("addition :",ret)



if __name__ == "__main__":
    main()