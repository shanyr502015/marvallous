import os

# def factorial(no):
#     fact = 1

#     for i in range(1, no+1):
#         fact = fact * i
#     return fact

def main():
    print(os.cpu_count()) # 8, cpu chi total noumber of cores - 8, cpu one asotoch

if __name__ == "__main__":
    main()

# enter number = 5000, bubble broke