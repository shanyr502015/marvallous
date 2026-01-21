import threading

icnt = 0
lobj = threading.Lock() # lock navacha class cha object banavala

def update():
    global icnt

    for _ in range(2000000):
        with lobj: # yachyasobat : with, with wala military man with lock 
            icnt = icnt + 1

def main():
    global icnt

    t1 = threading.Thread(target=update)
    t2 = threading.Thread(target=update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("value of icnt is :", icnt)

if __name__ == "__main__":
    main()