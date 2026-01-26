# python3 5_command_lineXXX.py 11 10
import sys

def main():
    # print("conmmand line arguments are : ")
    
    # for i in range(len(sys.argv)):
    #     print(sys.argv[i])
    #     return sys.argv[1] + sys.argv[2]
    no1 = int(sys.argv[1])
    no2 = int(sys.argv[2])

    print(no1 + no2)

if __name__ == "__main__":
    main()