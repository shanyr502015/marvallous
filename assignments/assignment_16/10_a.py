# Write a program which accept name from user and display length of its name.
# Input : Marvellous               Output : 10

def nametonum(name):
    # print(len(name))
    num = len(name)
    return num


def main():
    name = input("enter you name : ")
    ret = nametonum(name)
    print (ret)


if __name__ == "__main__":
    main()