import threading 

def display(no):
    print("inside display :",no)

    
def main():
    t = threading.Thread(target=display,args=(11,)) # hospital madhe apan tiffin staff laa detoh for our patient
    # t.start
    t.start()



if __name__ == "__main__":
    main()