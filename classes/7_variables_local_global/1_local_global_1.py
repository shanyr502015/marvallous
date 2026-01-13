# scope = limit 
no = 11 # global, data definition statement, sim card with roaming pack internationa call allowed, no privacy accesseable to all
def fun():
    no =21 # local, data definition statement, sim card indian
    print("value of no from fun is : ", no) # 21

print("value of no is : ", no) # 11
fun()

# global - out no need global keyword, inside it needed