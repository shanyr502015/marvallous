# one fucntion can call another function

def fun():
    print("inside fun")

def gun():
    print("inside gun")
    gun()

def main():
    fun()


if __name__ == "__main__": 
    main()
