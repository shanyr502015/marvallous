import time 
import datetime
import schedule

def fun():
    print("inside fun at :",datetime.datetime.now())
    
def main():
    print("inside marvallous automationscript at :",datetime.datetime.now())

    schedule.every(20).seconds.do(fun) # s wala seonds gya , second haa nahi

# there is problem in this code see 9_.py file
if __name__ == "__main__":
    main()