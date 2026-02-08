import os

def directoryScanner(Directoryname):
    print("contents of directory are :")

    for Foldername, SubFoldername, FileName in os.walk(Directoryname):
        print("folder name :", Foldername)

        for subf in SubFoldername:
            print("subfolder name :", SubFoldername)
        
        for fname in FileName:
            print("file name :",FileName)


def main():
    Directoryname = input("enter name of directory: ")
    directoryScanner(Directoryname)


if __name__ == "__main__":
    main()