def sumcube(no):
    sum = 0

    for i in range (1, no+1): # i haa for cha local variable ahe
        sum = sum + (i*i*i) # (i**3)

    return sum


def main():
    ret = sumcube(10)

    print (ret)


if __name__ == "__main__":
    main()