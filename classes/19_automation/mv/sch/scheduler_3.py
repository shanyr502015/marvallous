# KeyboardInterrupt --> ctrl + C
import time 
import datetime
import schedule

def fun():
    print("inside fun at :",datetime.datetime.now())
    
def main():
    print("inside marvallous automationscript at :",datetime.datetime.now())

    schedule.every(10).seconds.do(fun) 

    while True :
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()