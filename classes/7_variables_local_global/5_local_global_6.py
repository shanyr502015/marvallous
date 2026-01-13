no = 11 
def fun():
    global no # no recreated , used already created
    print("value of no from fun is : ", no)  
    no = no + 1
    print("value of no from fun is : ", no)

print("value of no is : ", no) 
fun()
print("value of no is : ", no) 

