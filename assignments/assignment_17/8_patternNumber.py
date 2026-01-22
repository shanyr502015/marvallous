# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

def patternNumber(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j, end=" " )
        print()

def main():
    num = int(input("enter number : "))
    patternNumber(num)

if __name__ == "__main__":
    main()