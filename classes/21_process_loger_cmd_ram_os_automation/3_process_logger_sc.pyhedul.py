# # command line input cha code ahe
# import psutil
# import sys
# import os
# import time
# import schedule





# def createlog(foldername):
#     if not os.path.exists(foldername):
#         os.mkdir(foldername)
#     # ret = False
#     # ret = os.path.exists(foldername)

#     # if (ret == True):
#     #     ret == os.path.isdir(foldername)
#     #     if (ret == False):
#     #         print("unable to create folder")
#     #         return
#     # else:
#     #     os.mkdir(foldername)
#     #     print("dir logs file crated")

#     timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
#     filename = os.path.join
#     print(timestamp)

#     fobj = open(filename,"w")
    

# def main():
#     border = "-"*50
#     print(border)
#     print("________mv platform surveillance system_______")
#     print(border)

#     if (len(sys.argv)==2):
#         if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
#             print("script is used to:")
#             print("1: create auto logs")
#             print("2: execute periodic")
#             print("3: send mail with log")
#             print("4: store info processesses")
#             print("5: store store info cpu")
#             print("6: store info ram usage")
#             print("7: store info second storage")

#         elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
#             print("use automation scritp")
#             print("scriptname.py timeinterval directoryname")
#             print("timeinterval: time in minute")
#             print("directorynmae : name of dir to create logs")

#         else: 
#             print ("unable to process")
#             print("use --h or --u to get details")

#     # python demo.py 5 mv
#     elif(len(sys.argv)==3):
#         print("inside project logic")
#         print("time interval:",sys.argv[1])
#         print("dir name:",sys.argv[2])
#         # createlog(sys.argv[2])
#         #apply schedule here
#         schedule.every(int(sys.argv[1])).minutes.do(createlog,sys.argv[2])
        
#         print("platform is running...")
#         print("dir created with :",sys.argv[2])
#         print("log created at every :",sys.argv[1]," minutes")
#         print("time interval is in minutes:",sys.argv[1])
#         print("ctrl + c to stop the process")


#         # wait till abort
#         while True:
#             schedule.run_pending()
#             time.sleep(1)

#     else:
#         print("invalid num of cmd")
#         print ("unable to process")
#         print("use --h or --u to get details")

#     print(border)
#     print("-------thank you for using our script--------")
#     print(border)

# if __name__ == "__main__":
#     main()

# command line input cha code ahe
import psutil
import sys
import os
import time
import schedule


def createlog(foldername):
    # Create folder if it doesn't exist
    if not os.path.exists(foldername):
        os.mkdir(foldername)

    # Create timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # FIX 1: Actually call os.path.join with proper arguments
    filename = os.path.join(foldername, f"log_{timestamp}.txt")
    print(f"Creating log: {filename}")

    # FIX 2: Use 'with' to auto-close file and write actual data
    with open(filename, "w") as fobj:
        # Write header
        fobj.write("=" * 50 + "\n")
        fobj.write("MV Platform Surveillance System Log\n")
        fobj.write("=" * 50 + "\n")
        fobj.write(f"Timestamp: {timestamp}\n\n")
        
        # CPU Info
        fobj.write("-" * 50 + "\n")
        fobj.write("CPU INFORMATION\n")
        fobj.write("-" * 50 + "\n")
        fobj.write(f"CPU Usage: {psutil.cpu_percent(interval=1)}%\n")
        fobj.write(f"CPU Count: {psutil.cpu_count()}\n\n")
        
        # Memory Info
        fobj.write("-" * 50 + "\n")
        fobj.write("MEMORY INFORMATION\n")
        fobj.write("-" * 50 + "\n")
        memory = psutil.virtual_memory()
        fobj.write(f"Total Memory: {memory.total / (1024**3):.2f} GB\n")
        fobj.write(f"Available Memory: {memory.available / (1024**3):.2f} GB\n")
        fobj.write(f"Memory Usage: {memory.percent}%\n\n")
        
        # Disk Info
        fobj.write("-" * 50 + "\n")
        fobj.write("DISK INFORMATION\n")
        fobj.write("-" * 50 + "\n")
        disk = psutil.disk_usage('/')
        fobj.write(f"Total Disk: {disk.total / (1024**3):.2f} GB\n")
        fobj.write(f"Used Disk: {disk.used / (1024**3):.2f} GB\n")
        fobj.write(f"Disk Usage: {disk.percent}%\n\n")
        
        # Process Info
        fobj.write("-" * 50 + "\n")
        fobj.write("PROCESS INFORMATION\n")
        fobj.write("-" * 50 + "\n")
        fobj.write(f"Running Processes: {len(psutil.pids())}\n")
        
        fobj.write("\n" + "=" * 50 + "\n")
    
    print(f"Log created successfully: {filename}")


def main():
    border = "-" * 50
    print(border)
    print("________mv platform surveillance system_______")
    print(border)

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("script is used to:")
            print("1: create auto logs")
            print("2: execute periodic")
            print("3: send mail with log")
            print("4: store info processesses")
            print("5: store store info cpu")
            print("6: store info ram usage")
            print("7: store info second storage")

        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("use automation script")
            print("scriptname.py timeinterval directoryname")
            print("timeinterval: time in minute")
            print("directoryname: name of dir to create logs")

        else: 
            print("unable to process")
            print("use --h or --u to get details")

    # python demo.py 5 mv
    elif (len(sys.argv) == 3):
        print("inside project logic")
        print("time interval:", sys.argv[1])
        print("dir name:", sys.argv[2])
        
        # Create first log immediately
        createlog(sys.argv[2])
        
        # Apply schedule here
        schedule.every(int(sys.argv[1])).minutes.do(createlog, sys.argv[2])
        
        print("platform is running...")
        print("dir created with:", sys.argv[2])
        print("log created at every:", sys.argv[1], "minutes")
        print("ctrl + c to stop the process")

        # Wait till abort
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nStopping the platform...")

    else:
        print("invalid num of cmd")
        print("unable to process")
        print("use --h or --u to get details")

    print(border)
    print("-------thank you for using our script--------")
    print(border)


if __name__ == "__main__":
    main()