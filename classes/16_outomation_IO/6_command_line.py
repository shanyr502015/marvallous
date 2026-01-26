# python3 5_command_lineXXX.py 11 10
# sys inbuild 
import sys

def main():
    # if (len(sys.argv)!=3):
    #     print("invalid number of arguments")

    if (len(sys.argv) < 3 or len(sys.argv) > 3 ):
        print("invalid number of arguments")
    else:
        no1 = int(sys.argv[1])
        no2 = int(sys.argv[2])

        print(no1 + no2)

if __name__ == "__main__":
    main()


# pypi - all modules in python site
# module - simpel .py file contain related funcntion , module type --> udf, inbuil, third party 
# pip  - utility , package installer for python, pip python chya installlation sobat yete in recent python version
# pip install pip laa recursion mantatat
# pip use - to in stall package, to upgrade package, to uninsall package (package = module)