data = [10,20,30,40,50]

for i in range(5):
    print(i)

for i in range(5):
    # print(i)
    print(data[i])

sum = 0
for i in range(5):
    # print(data[i])
    sum = sum + data[i]
print("sumation :", sum)