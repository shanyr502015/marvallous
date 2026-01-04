# one fucntion can call another function
# use return keyword if want to return value oterwise no need

def fun():
    print("inside fun")

def gun():
    print("inside gun")

def main():
    fun()
    gun()


if __name__ == "__main__": 
    main()
