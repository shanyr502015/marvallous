# Write a program which display first 10 even numbers on screen.
# Output : 2   4   6   8   10   12   14   16   18   20

def first10evennumbers():
    for i in range(2,21,2):
        print(i,end = " ")


def main():
    first10evennumbers()



if __name__ == "__main__":
    main()