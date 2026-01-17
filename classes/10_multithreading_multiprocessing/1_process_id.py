# process: pid, every process has unique number that one is pid
# thread : tid, every thread has unique number that one is tid

# pvm handdle process considerng its PID number not with name like addhar card number imp and unique, 
# you can see duplicate name but adhar cared number


import os # inbuild module, if third party error if not downloaded(pip)


def main():
    # print("pid of running proces is :", os.getpid)
    # print("pid of parent process is :", os.getppid)
    print("pid of running proces is :", os.getpid())
    print("pid of parent process is :", os.getppid())

if __name__ == "__main__":
    main()
 # hotel mangt - os, you given room with specific room - room with rooom number
 # time complexity decided on basis of look
 # time execution(start to end time) is not time complexity