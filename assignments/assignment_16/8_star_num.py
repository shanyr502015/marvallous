# Write a program which accept number from user and print that number of "*" on screen.
# Input : 5                        Output : *   *   *   *   *


def convertStar(no):
    for i in range (1, no+1):
        print ("*", end=" ")

def main():
    num = int(input("enter number here: "))
    ret = convertStar(num)


if __name__ == "__main__":
    main()