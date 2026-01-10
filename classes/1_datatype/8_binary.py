data = bytes([65])
print(data)  # b'A', b for binary , A asch value
print(type(data))

##### binaryX ##########
#################
# Indexed
# ordered
# Immutable
data = bytes([65])
print(data)
print(type(data))
print(data[0])

data = bytes([65,97,98])
print(data)
print(type(data))
print(data[0])


data[0] = 66
print(data[0]) # error, TypeError: 'bytes' object does not support item assignment(immutable)




##### binaryXX ##########
# Indexed
# ordered
# Immutable
data = bytearray([65])
print(data)
print(type(data))
print(data[0])

data = bytes([65,97,98])
print(data)
print(type(data))
print(data[0])


data[0] = 66
print(data[0]) # error, TypeError: 'bytes' object does not support item assignment(immutable)
