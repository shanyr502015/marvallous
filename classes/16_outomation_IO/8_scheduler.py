# import datetime
# import schedule

# def fun():
#     print("inside fun at :",datetime.datetime.now())
    
# def main():
#     print("inside marvallous automationscript at :",datetime.datetime.now())

#     schedule.every(10).seconds.do(fun) # "with s" wala seconds gya , second haa nahi  " without s" wala nahi

# # there is problem in this code we see in 9_scheduler.py file
# if __name__ == "__main__":
#     main()



import datetime
import schedule
import time

def fun():
    print("inside fun :" , datetime.datetime.now())

def gun():
    print("inside gun at :",datetime.datetime.now())

def main():
    print("inside main :",datetime.datetime.now())
    schedule.every(2).seconds.do(fun)
    schedule.every(3).seconds.do(gun)

    while True :
        schedule.run_pending()
        time.sleep(1)


main()