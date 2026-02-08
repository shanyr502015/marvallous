import sys

def main():
    print(sys.argv)
    print(sys.argv[0]) # 3_command_lineX.py // here module chaa data use karat ahe module call karat nahi ahe
    print(len(sys.argv)) # 1

if __name__ == "__main__":
    main()