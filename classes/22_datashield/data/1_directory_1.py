import os
def main():
    Directoryname = input("Enter name of directory: ")
    
    # Check if the directory actually exists to avoid errors
    if not os.path.exists(Directoryname):
        print("Invalid directory path.")
        return

    print("Contents of directory are :")

    for Foldername, SubFoldername, FileName in os.walk(Directoryname):
        print("\nFolder name :", Foldername)

        for subf in SubFoldername:
            # Use the iterator 'subf', not the list 'SubFoldername'
            print("Subfolder name :", subf)

        for fname in FileName:
            # Use the iterator 'fname', not the list 'FileName'
            print("File name :", fname)

if __name__ == "__main__":
    main()