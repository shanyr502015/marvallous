# keyboardinterrupt --> ctrl + C
import time 
import datetime
import schedule

def fun():
    print("inside fun at :",datetime.datetime.now())
    
def main():
    print("inside marvallous automationscript at :",datetime.datetime.now())

    schedule.every(20).seconds.do(fun) # s wala seonds gya , second haa nahi

    while True :
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()