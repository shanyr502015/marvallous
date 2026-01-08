# nested funciton only in  python
def phoenix(): 
    print("inside phoenix")

    def zara():
        print("inside zara")
        # zara() # recursive fucntion
    zara() # nested fucniton

def main():
    phoenix()
   

if __name__ == "__main__": 
    main()

# funciton can return anoter fuction we can see latter.