# ============================================================
# Project : Marvellous Platform Surveillance System
# Purpose : Periodic system monitoring with clear memory logs
# ============================================================

import psutil
import sys
import os
import time
import schedule

# ------------------------------------------------------------
# Function Name : CreateLog
# Purpose       : Creates log file and writes system information
# ------------------------------------------------------------
def CreateLog(FolderName):
    Border = "-" * 50
    Ret = False

    # Directory handling
    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created succesfully")

    # Log file creation
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)
    print("Log file gets created with name : ", FileName)

    fobj = open(FileName, "w")

    # Header
    fobj.write(Border + "\n")
    fobj.write("---- Marvellous Platform Surveillance System -----\n")
    fobj.write("Log created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    # ================= SYSTEM REPORT =================
    fobj.write("----------------- System Report ------------------\n")
    fobj.write(Border + "\n")

    # CPU Usage
    cpu = psutil.cpu_percent()
    fobj.write("CPU Usage : %s %%\n" % cpu)
    fobj.write(Border + "\n")

    # ================= MEMORY (RAM) LOGS =================
    mem = psutil.virtual_memory()

    fobj.write("Memory (RAM) Usage Details\n")
    fobj.write(Border + "\n")

    fobj.write("Total RAM      : %.2f GB\n" % (mem.total / (1024 ** 3)))
    fobj.write("Used RAM       : %.2f GB\n" % (mem.used / (1024 ** 3)))
    fobj.write("Available RAM  : %.2f GB\n" % (mem.available / (1024 ** 3)))
    fobj.write("RAM Usage      : %s %%\n" % mem.percent)

    fobj.write(Border + "\n")

    # ================= DISK USAGE =================
    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border + "\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border + "\n")

    # ================= NETWORK USAGE =================
    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border + "\n")

    # Footer
    fobj.write(Border + "\n")
    fobj.write("----------------- End of Log File ----------------\n")
    fobj.write(Border + "\n")

    fobj.close()

# ------------------------------------------------------------
# Function Name : main
# Purpose       : Entry point of application
# ------------------------------------------------------------
def main():
    Border = "-" * 50
    print(Border)
    print("---- Marvellous Platform Surveillance System -----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Store CPU, Memory, Disk and Network usage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")

        else:
            print("Invalid option")

    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System started succesfully")
        print("Press Ctrl + C to stop the execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)

# ------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()