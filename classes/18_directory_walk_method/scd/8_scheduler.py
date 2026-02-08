import datetime
import schedule

def fun():
    print("inside fun at :",datetime.datetime.now())
    
def main():
    print("inside marvallous automationscript at :",datetime.datetime.now())

    schedule.every(10).seconds.do(fun) # "with s" wala seconds gya , second haa nahi  " without s" wala

# there is problem in this code we see in 9_scheduler.py file
if __name__ == "__main__":
    main()