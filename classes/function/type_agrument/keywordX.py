def employeeinfo(name,age,salary,city):
    print("name :", name)
    print("age :", age)
    print("salary :", salary)
    print("city :", city)

def main():
    # keyword argument
    employeeinfo(age=26,name="rahul",city="pune",salary=None) # correct, due to python dynamically typed language

if __name__ == '__main__':
    main()