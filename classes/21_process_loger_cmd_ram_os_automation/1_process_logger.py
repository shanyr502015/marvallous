# command line input cha code ahe
import psutil
import sys

def main():
    border = "-"*50
    print(border)
    print("________mv platform surveillance system_______")
    print(border)

    if (len(sys.argv)==2):
        if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("script is used to:")
            print("1: create auto logs")
            print("2: execute periodic")
            print("3: send mail with log")
            print("4: store info processesses")
            print("5: store store info cpu")
            print("6: store info ram usage")
            print("7: store info second storage")

        elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("use automation scritp")
            print("scriptname.py timeinterval directoryname")
            print("timeinterval: time in minute")
            print("directorynmae : name of dir to create logs")

        else: 
            print ("unable to process")
            print("use --h or --u to get details")

    # python demo.py 5 mv
    elif(len(sys.argv)==3):
        print("inside project logic")
        print("time interval:",sys.argv[1])
        print("dir name:",sys.argv[2])

    else:
        print("invalid num of cmd")
        print ("unable to process")
        print("use --h or --u to get details")

    print(border)
    print("-------thank you for using our script--------")
    print(border)

if __name__ == "__main__":
    main()