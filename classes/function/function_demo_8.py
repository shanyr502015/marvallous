# accept: multiples parameters
# return : multiple value (only in python allowed)
def marvallous1(value1, value2):
    print("inside marvallou1 :", value1, value2)
    return 11, 21, 51

def main():
    result1 = None
    result2 = None
    result3 = None

    result1, result2, result3 = marvallous1("python", 21)
    print("return value :", result1, result2, result3)

if __name__ == "__main__": 
    main()