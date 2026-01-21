icnt = 0

def update():
    global icnt

    for _ in range(2000000):
        icnt = icnt + 1

def main():
    global icnt

    update() # 200000
    update() # 400000

    print("value of icnt is :", icnt)

if __name__ == "__main__":
    main()