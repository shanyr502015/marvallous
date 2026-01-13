def checkeven(no):
    return (no % 2 == 0)

def main():
    data = [11,10,15,20,22,27,30]
    print ("actual data :", data)

    # fdata = filter(checkeven, data) # memory of filter
    fdata = list(filter(checkeven, data)) # filter typecast in list, # append karnay ahe # chceksum () - calling as functino so here given as checksum as parameter
    print("data after filer is :", fdata)

if __name__ == "__main__":
    main()
