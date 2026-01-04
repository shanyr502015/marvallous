# accept: multiples parameters
# return : one value
def marvallous1(value1, value2):
    print("inside marvallou1 :", value1, value2)
    return 11

def main():
    result = None
    result = marvallous1("python", 21)
    print("return value :", result)

if __name__ == "__main__": 
    main()