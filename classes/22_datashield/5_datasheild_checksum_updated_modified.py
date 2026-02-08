# daatshield
import sys
import os
import time
import schedule
import shutil
import hashlib

def calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()
    return hobj.hexdigest()

def backupfiles(source,destination):
    copied_files = []

    print("Backing up files from", source, "to", destination)
    os.makedirs(destination, exist_ok=True)

    for root, dirs, files in os.walk(source):
        for file in files:
            src_path = os.path.join(root, file)

            relative = os.path.relpath(src_path, source)
            dest_path = os.path.join(destination, relative)

            # Create destination subdirectories if they don't exist
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # copy file if its new or updated
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files

def mvdatashieldstart(source = "data"):
    backupname = "mvbackup"
    print("backup started successfully at:", time.strftime("%Y-%m-%d %H:%M:%S"))

    # backupfiles(source,backupname)
    files = backupfiles(source,backupname)
    print("reports about backup")
    for f in files:
        print(f"Backed up: {f}")


def main():
    border = "-" * 50

    print(border)
    print("________MV Data Shield_______")
    print(border)

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Script is used to:")
            print("1: takes auto backup at given time")
            print("2: bakcup only and updated files")
            print("3: create and archive backup periodically")

        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use automation script:")
            print("scriptname.py timeinterval source dir")
            print("timeinterval: Time in minutes")
            print("sourcedirectory: name of dir to backed up")

        else: 
            print("Unable to process")
            print("Use --h or --u to get details")

    # python demo.py 5 data
    elif (len(sys.argv) == 3):
        print("Inside project logic")
        print("Time interval:", sys.argv[1])
        print("Directory name:", sys.argv[2])

        
        # Apply schedule here
        schedule.every(int(sys.argv[1])).minutes.do(mvdatashieldstart,sys.argv[2])
        
        print("\n Data shield system running...")
        print("time interval:", sys.argv[1])
        print("Press Ctrl + C to stop the process")

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