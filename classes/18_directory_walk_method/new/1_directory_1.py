import os
def main():
    Directoryname = input("enter name of directory")
    print("contents of directory are :")

    for Foldername, SubFoldername, FileName in os.walk(Directoryname):
        print("folder name :", Foldername)

        for subf in SubFoldername:
            print("subfolder name :", SubFoldername)
        
        for fname in FileName:
            print("file name :",FileName)


if __name__ == "__main__":
    main()