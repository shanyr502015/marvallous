# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
# *   *   *   *   *
# *   *   *   *
# *   *   *
# *   *
# *

def display(no):
    for i in range (no, 0, -1):
        for j in range (i):
            print("*",end=" ")
        print()


##########################################
# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *

def pattern(no):
    for i in range(no):
        for j in range(no):
            print("*",end = " ")
        print() #  # New line after each row

def main():
    num = int (input("enter number here : "))
    display(num)
    print("-------------------------------")
    pattern(num)

if __name__ == "__main__":
    main()