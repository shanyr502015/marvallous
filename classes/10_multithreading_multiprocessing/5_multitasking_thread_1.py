import threading 

# syncronization in threading not in processing
# critical section, part of code has to executed one thread at time
# rest condition- 

def display(): # callback funciton - lihatoh pan call nahi karat, pan baherun karotoh
    print("inside display :", threading.get_ident())


def main():
    print("inside main :", threading.get_ident())
    t = threading.Thread(target=display) # thread banatoh
    t.start() # thread start hoto
    print ("end of main")


if __name__ == "__main__":
    main()