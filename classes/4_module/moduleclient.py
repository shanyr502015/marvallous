# user of marvallous module (client)
import marvallous

print("inside client: ",__name__)
print("value fo PI is :", marvallous.PI)

result = 0
result = marvallous.add(11,10)
print("addition is : ",result)


result = marvallous.sub(11,10)
print("subtraction is : ",result)