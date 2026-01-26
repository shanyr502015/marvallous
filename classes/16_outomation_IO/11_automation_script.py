# hooking, --h --> help, --u --> usage
import sys

def main():
    border = "_"*40
    print(border)
    print("--------------------mv------------------")
    print(border)

    if (len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H") ):
            print("this applicaiton use to perform ________")
            print("this is automation script")

        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U") ):
            print("use the given script as")
            print("scriptname.py argument1 argument2")
            print("argument1 : _______")
            print("argument1 : _______")

        else:
            print("use given flag as :s")
            print("--u : used to dispaly the usage")
            print("--h : used to dispaly the help")
    else:
        print("invalid number of command line arguments")
        print("use given flag as :")
        print("--u : used to dispaly the usage")
        print("--h : used to dispaly the help")
    
    print(border)
    print("----thank you for using our script------")
    print("----------------mv_info-----------------")
    print(border)


if __name__ == "__main__":
    main()