import threading 

def display(): # callback funciton - lihatoh pan call nahi karat, pan baherun karotoh
    print("inside display :", threading.get_ident())
    for i in range(100):
        print("inside display")


def main():
    print("inside main :", threading.get_ident())
    t = threading.Thread(target=display) # thread banatoh
    t.start() # thread start hoto
    print ("end of main")


if __name__ == "__main__":
    main()


# 