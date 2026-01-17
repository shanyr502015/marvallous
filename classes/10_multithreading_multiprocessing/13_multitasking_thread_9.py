import threading 
import time

def sumeven(no):
    sum = 0
    for i in range(2, no+1 ,2):
        sum = sum + i
    print("enen sum is :", sum)
    
def sumodd(no):
    sum = 0
    for i in range(1, no+1, 2):
        sum = sum = 1
    print("odd sum is :",sum)
    
def main():
    start_time = time.time()

    t1 = threading.Thread(target=sumeven,args=(1000000,))
    t2 = threading.Thread(target=sumodd,args=(1000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time() 

    print("time required :", end_time - start_time)


if __name__ == "__main__":
    main()