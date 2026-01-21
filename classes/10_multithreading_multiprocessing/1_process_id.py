# process: pid, every process has a unique number which is called pid
# thread: tid, every thread has a unique number which is called tid

 # PVM handles processes considering their PID number, not with name - like Aadhaar card number, important and unique
 # you can see duplicate names but Aadhaar card numbers are unique


import os  # inbuilt module, if third party - error if not downloaded (pip)


def main():
    # print("pid of running process is :", os.getpid)
    # print("pid of parent process is :", os.getppid)
    print("pid of running process is :", os.getpid())
    print("pid of parent process is :", os.getppid())

if __name__ == "__main__":
    main()
# hotel management - OS is like a hotel manager, you are given a room with a specific room number (PID)
# Just like multiple guests can have the same name, but each room has a unique room number, multiple processes can have the same name, but each process has a unique PID
# EXTRA: time complexity is decided on the basis of loops, time execution (start to end time) is not time complexity