import threading 

def display(no1,no2,no3):
    print("inside display :",no1, no2, no3)

    
def main():
    t = threading.Thread(target=display,args=(11,21,31,)) # hospital madhe apan tiffin staff laa detoh for our patient
    # t.start
    t.start()



if __name__ == "__main__":
    main()