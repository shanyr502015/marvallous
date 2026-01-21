# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise false.
# Input : 8                        Output : False
# Input : 25                       Output : True

def CheckDivisible (no):
    if no % 5 == 0:
        return True
    else:
        return False


def main():
    num = int(input("enter number : "))
    ret = CheckDivisible (num)
    print(ret)


if __name__ == "__main__":
    main()
