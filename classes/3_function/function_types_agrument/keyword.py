def employeeinfo(name,age,salary,city):
    print("name :", name)
    print("age :", age)
    print("salary :", salary)
    print("city :", city)

def main():
    # positional
    employeeinfo("rahul",26,2000.50,"puen") # correct
    print("--------------")
    employeeinfo(26,"rahul","puen",2000.50) # wrong
    print("--------------")
    # keyword argument
    employeeinfo(age=26,name="rahul",city="pune",salary=2000.50) # correct

if __name__ == '__main__':
    main()