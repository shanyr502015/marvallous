# nested funciton only in  python
def phoenix(): 
    print("inside phoenix")
    def zara():
        print("inside zara")

# def main():
#     zara() # nameerror: name "zara" not defined

def main():
    phoenix.zara() # attributeerror: 'funciton' object has no attribute "zara"
   


if __name__ == "__main__": 
    main()
