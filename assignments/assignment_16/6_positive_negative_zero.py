# Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11                       Output : Positive Number
# Input : -8                       Output : Negative Number
# Input : 0                        Output : Zero

def chknum(no):
    if no > 0 :
        print("Positive Number")
    elif no < 0 :
        print("Negative Number")
    else:
        print("Zero")


def main():
    num = int(input("enter number :"))
    chknum(num)
    # ret = chknum(num)
    # print(ret)


if __name__ == "__main__":
    main()