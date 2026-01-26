import time 
import datetime
import schedule

def fun():
    print("inside fun at :",datetime.datetime.now())

def gun():
    print("inside gun at :",datetime.datetime.now())
    
    
def main():
    print("inside marvallous automationscript at :",datetime.datetime.now())

    # schedule.every(20).seconds.do(fun) 
    schedule.every(2).seconds.do(fun)
    schedule.every(3).seconds.do(gun)

    while True :
        schedule.run_pending()
        time.sleep(1)
        # time.sleep(50)
        
if __name__ == "__main__":
    main()