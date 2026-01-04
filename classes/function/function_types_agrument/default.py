def employeeinfo(name="gotya",age=21,salary=1000,city="pune"):
    print("name :", name)
    print("age :", age)
    print("salary :", salary)
    print("city :", city)

def main():
    # employeeinfo(age=26,name="rahul",city="pune",salary=2000.50) # keyword argument
    employeeinfo() # default agrument

if __name__ == '__main__':
    main()