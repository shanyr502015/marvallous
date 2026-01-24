class demo:
    no = 10
    
    def __init__(self,a,b):
        self.value1 = a
        self.value2 = b

    def fun (self):
        # print("inside instance method fun")
        print("inside instance method fun :",self.value1,self.value2)

    @classmethod # decorator = lal diwas, inbuilt decorator ahe ha - @classmethod
    def sun(cls):
        # print("inside class method sun ")
        print("inside class method sun : ",cls.no)

demo.sun() 
print ("class variable no :",demo.no)

obj = demo(11,21)

obj.fun()
print("instnce variable :", obj.value1, obj.value2)

#  decorator - lal diwa gadi - officer vechicle not normall vehicle, two type - udf and inbuild, diwa in pyhton = @