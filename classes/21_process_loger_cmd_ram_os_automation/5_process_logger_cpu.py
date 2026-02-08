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
    
    # Create filename
    filename = os.path.join(foldername, f"log_{timestamp}.txt")
    print(f"Creating log: {filename}")

    # Write to file with proper header and footer
    with open(filename, "w") as fobj:
        # ============================================
        # HEADER SECTION
        # ============================================
        fobj.write("\n\n")  # Empty lines at top
        fobj.write("=" * 70 + "\n")
        fobj.write(" " * 15 + "MV PLATFORM SURVEILLANCE SYSTEM\n")
        fobj.write(" " * 25 + "LOG FILE\n")
        fobj.write("=" * 70 + "\n")
        fobj.write(f"Generated On: {time.strftime('%Y-%m-%d')}\n")
        fobj.write(f"Generated At: {time.strftime('%H:%M:%S')}\n")
        fobj.write(f"Log Timestamp: {timestamp}\n")
        fobj.write("=" * 70 + "\n")
        fobj.write("\n\n")  # Empty lines after header
        
        # ============================================
        # BODY SECTION - SYSTEM INFORMATION
        # ============================================
        
        # CPU Information
        fobj.write("-" * 70 + "\n")
        fobj.write("CPU INFORMATION\n")
        fobj.write("-" * 70 + "\n")
        fobj.write(f"CPU Usage: {psutil.cpu_percent(interval=1)}%\n")
        fobj.write(f"CPU Count (Physical): {psutil.cpu_count(logical=False)}\n")
        fobj.write(f"CPU Count (Logical): {psutil.cpu_count(logical=True)}\n")
        fobj.write("\n")
        
        # Memory Information
        fobj.write("-" * 70 + "\n")
        fobj.write("MEMORY (RAM) INFORMATION\n")
        fobj.write("-" * 70 + "\n")
        memory = psutil.virtual_memory()
        fobj.write(f"Total Memory: {memory.total / (1024**3):.2f} GB\n")
        fobj.write(f"Available Memory: {memory.available / (1024**3):.2f} GB\n")
        fobj.write(f"Used Memory: {memory.used / (1024**3):.2f} GB\n")
        fobj.write(f"Memory Usage: {memory.percent}%\n")
        fobj.write("\n")
        
        # Disk Information
        fobj.write("-" * 70 + "\n")
        fobj.write("SECONDARY STORAGE (DISK) INFORMATION\n")
        fobj.write("-" * 70 + "\n")
        disk = psutil.disk_usage('/')
        fobj.write(f"Total Disk Space: {disk.total / (1024**3):.2f} GB\n")
        fobj.write(f"Used Disk Space: {disk.used / (1024**3):.2f} GB\n")
        fobj.write(f"Free Disk Space: {disk.free / (1024**3):.2f} GB\n")
        fobj.write(f"Disk Usage: {disk.percent}%\n")
        fobj.write("\n")
        
        # Process Information
        fobj.write("-" * 70 + "\n")
        fobj.write("PROCESS INFORMATION\n")
        fobj.write("-" * 70 + "\n")
        fobj.write(f"Total Running Processes: {len(psutil.pids())}\n")
        fobj.write("\n")
        
        # Top 5 Processes by Memory Usage
        fobj.write("Top 5 Processes by Memory Usage:\n")
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Sort by memory usage and get top 5
        processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]
        for i, proc in enumerate(processes, 1):
            fobj.write(f"  {i}. {proc['name']} (PID: {proc['pid']}) - {proc['memory_percent']:.2f}%\n")
        
        fobj.write("\n")
        
        # ============================================
        # FOOTER SECTION
        # ============================================
        fobj.write("\n\n")  # Empty lines before footer
        fobj.write("=" * 70 + "\n")
        fobj.write(" " * 25 + "END OF LOG FILE\n")
        fobj.write("=" * 70 + "\n")
        fobj.write(f"Log file closed at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        fobj.write("=" * 70 + "\n")
        fobj.write("\n\n")  # Empty lines at bottom

        print("cpu ")
    
    print(f"Log created successfully: {filename}")


def main():
    border = "-" * 50
    print(border)
    print("________MV PLATFORM SURVEILLANCE SYSTEM_______")
    print(border)

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Script is used to:")
            print("1: Create auto logs")
            print("2: Execute periodic monitoring")
            print("3: Send mail with log")
            print("4: Store info about processes")
            print("5: Store info about CPU")
            print("6: Store info about RAM usage")
            print("7: Store info about secondary storage")

        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use automation script:")
            print("scriptname.py timeinterval directoryname")
            print("timeinterval: Time in minutes")
            print("directoryname: Name of directory to create logs")

        else: 
            print("Unable to process")
            print("Use --h or --u to get details")

    # python demo.py 5 mv
    elif (len(sys.argv) == 3):
        print("Inside project logic")
        print("Time interval:", sys.argv[1])
        print("Directory name:", sys.argv[2])
        
        # Create first log immediately
        createlog(sys.argv[2])
        
        # Apply schedule here
        schedule.every(int(sys.argv[1])).minutes.do(createlog, sys.argv[2])
        
        print("\nPlatform is running...")
        print("Directory created with:", sys.argv[2])
        print("Log created at every:", sys.argv[1], "minutes")
        print("Press Ctrl + C to stop the process\n")

        # Wait till abort
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nStopping the platform...")

    else:
        print("Invalid number of arguments")
        print("Unable to process")
        print("Use --h or --u to get details")

    print(border)
    print("-------THANK YOU FOR USING OUR SCRIPT--------")
    print(border)


if __name__ == "__main__":
    main()