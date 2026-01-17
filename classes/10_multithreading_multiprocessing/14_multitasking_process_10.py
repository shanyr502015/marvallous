import multiprocessing
import time
import os

def sumeven(no):
    print("pid of sumevne:",os.getpid()) # 51, imagine
    print("ppid of sumevne:",os.getppid()) # 21
    sum = 0
    for i in range(2, no+1 ,2):
        sum = sum + i

    print("enen sum is :", sum)
    
def sumodd(no):
    print("pid of sumodd:",os.getpid()) # 101 , imagine
    print("ppid of sumodd:",os.getppid()) # 21
    sum = 0
    for i in range(1, no+1, 2):
        sum = sum = 1

    print("odd sum is :",sum)
    
def main():
    print("pid of main:",os.getpid()) # 21 imagine
    print("ppid of main:",os.getppid()) # cmd 11 imagine
    start_time = time.time()

    t1 = multiprocessing.Process(target=sumeven,args=(1000000,))
    t2 = multiprocessing.Process(target=sumodd,args=(1000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time() 

    print("time required :", end_time - start_time)


if __name__ == "__main__":
    main()