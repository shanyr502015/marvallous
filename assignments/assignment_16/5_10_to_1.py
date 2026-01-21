# Write a program which display 10 to 1 on screen.
# Output : 10   9   8   7   6   5   4   3   2   1

def display():
    for i in range(10, 0, -1):
        # print (i)
        print(i, end=" ")

def main():
    display()

if __name__ == "__main__":
    main()
# -------------------------------
# def display(lst):
#     lst.reverse()
#     return lst


# def main():
#     lst = [1,2,3,4,5,6,7,8,9,10]
#     ret = display(lst)
#     print(ret)


# if __name__ == "__main__":
#     main()

# -------------------------------
# def display(lst):
#     reversed_lst = []
#     for i in range(len(lst),0,-1):
#     # for i in range(len(lst)-1,-1,-1):
#         # reversed_lst.append(lst)
#         reversed_lst.append(i)
#     return reversed_lst


# def main():
#     lst = [1,2,3,4,5,6,7,8,9,10]
#     ret = display(lst)
#     print(ret)


# if __name__ == "__main__":
#     main()
