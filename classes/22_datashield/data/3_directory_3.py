# import os

# def directoryScanner(Directoryname="mv"):
#     ret = os.path.exists(Directoryname)
#     if (ret == False):
#         print("there is no such dir")
#         return
#     ret = os.path.isdir(Directoryname)
#     if ret == False:
#         print("unable to scan its not directoy")
#         return
#     print("contents of directory are :")
#     for Foldername, SubFoldername, FileName in os.walk(Directoryname):
#         print("folder name :", Foldername)
#         for subf in SubFoldername:
#             print("subfolder name :", SubFoldername)
#         for fname in FileName:
#             print("file name :",FileName)
# def main():
#     Directoryname = input("enter name of directory: ")
#     directoryScanner(Directoryname)
# if __name__ == "__main__":
#     main()

import os

def directoryScanner(Directoryname):
    # Check if the path exists before scanning
    if not os.path.exists(Directoryname):
        print("Error: The directory does not exist.")
        return

    print("contents of directory are :")

    for Foldername, SubFoldername, FileName in os.walk(Directoryname):
        print("\nfolder name :", Foldername)

        for subf in SubFoldername:
            # Use the single item 'subf', not the whole list
            print("subfolder name :", subf)

        for fname in FileName:
            # Use the single item 'fname', not the whole list
            print("file name :", fname)

def main():
    Directoryname = input("enter name of directory: ")
    # Press the "start button" by calling the function
    directoryScanner(Directoryname)

if __name__ == "__main__":
    main()