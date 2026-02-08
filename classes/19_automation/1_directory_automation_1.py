# import sys
# import os
# def directoryscanner(dirname = "mv"):
#     ret = False
#     ret = os.path.exists(dirname)
#     if (ret == False):
#         print("there is no such dir")
#         return
#     ret = os.path.isdir(dirname)
#     if ret == False :
#         print("id is not dir")
#         return
#     for foldername, subfolder, filename in os.walk(dirname):
#         for fname in filename:
#             print("fname")
# def main():
#     border = "_"*50
#     print(border)
#     print("----------------mv dir automation-----------------")
#     print(border)
#     if (len(sys.argv) != 2):
#         print("invalid number fo arguments")
#         print("please specify name of dir")
#         return
#     directoryscanner(sys.argv[1])
# if __name__ == "__main__":
#     main()

import os
import sys

def directoryScanner(dirname):
    # Check if the directory exists and is actually a directory
    if not os.path.exists(dirname):
        print("Error: Path does not exist.")
        return
    if not os.path.isdir(dirname):
        print("Error: This is not a directory.")
        return

    print(f"--- Contents of {dirname} ---")
    for foldername, subfolders, filenames in os.walk(dirname):
        print("\nFolder:", foldername)

        for subf in subfolders:
            print("  Subfolder:", subf)  # Prints the item, not the list

        for fname in filenames:
            print("  File:", fname)       # No quotes around fname

def main():
    border = "_" * 50
    print(border)   
    print("----------------mv dir automation-----------------")
    print(border)
    # If you want to use command line arguments (like in your 3rd image)
    if len(sys.argv) == 2:
        directoryScanner(sys.argv[1])
    else:
        # Fallback to manual input if no argument is provided
        d_name = input("Enter name of directory: ")
        directoryScanner(d_name)

if __name__ == "__main__":
    main()