import time
import os
def sumcube(no):
    sum = 0
    print("process is running with PID :",os.getpid())
    for i in range (1, no+1):
        sum = sum + (i**3) 

    return sum


def main():
    # data = [100000,200000,300000,400000, 500000,600000,700000,800000,900000,1000000]
    data = [1000000,2000000,3000000,4000000, 5000000,6000000,7000000,8000000,9000000,10000000] #8.13 sec
    result = []
    
    start_time = time.time()

    for i in range(len(data)):
        ret = sumcube(data[i])
        result.append(ret)

    end_time = time.time()

    print(result)
    print("total execution time :", end_time-start_time)


if __name__ == "__main__":
    main()