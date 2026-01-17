import threading 

def display(): # callback funciton - lihatoh pan call nahi karat, pan baherun karotoh
    for i in range(10):
        print("inside display :", threading.get_ident())


def main():
    print("inside main :", threading.get_ident())

    t1 = threading.Thread(target=display) # thread banatoh
    t1.start() # thread start hoto
    
    t2 = threading.Thread(target=display)
    t2.start() 

    t1.join() # main stop unstill t thread finishe becoz of this join
    t2.join() 
    
    print ("end of main")


if __name__ == "__main__":
    main()