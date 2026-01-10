information = {"name":"rahul","age":25,"city":"pune","marks":89.90 }
print(type(information)) # mapping, dict
print(information) # {'name': 'rahul', 'age': 25, 'city': 'pune', 'marks': 89.9}
print(information["city"]) # pune, access via key, not index.
 # mutable , value can change that's why mutable
information["age"]=26
print(information) # {'name': 'rahul', 'age': 26, 'city': 'pune', 'marks': 89.9}    
# unordered but sequencial access via key.          


##### mappingX ##########
information = {"name":"rahul","age":25,"city":"pune","marks":89.90,"city":"mumbai"}
# print(type(information))
print(information)
print(information["city"])
information["age"]=26
print(information) # mutable , value can change that's why mutable


######### mappingXX ##########
d = {
    "name": "A",     
    10: "ten", 
    3.14: "pi",
    True: "yes",
    (1, 2): "tuple key",
    frozenset({1, 2}): "frozen set key",
    None: "null"
}
print(d) # {'name': 'A', 10: 'ten', 3.14: 'pi', True: 'yes', (1, 2): 'tuple key', frozenset({1, 2}): 'frozen set key', None: 'null'}
print(d["name"]) # A
print(d[10]) # ten
print(d[3.14]) # pi
print(d[True]) # yes    
print(d[(1, 2)]) # tuple key
print(d[frozenset({1, 2})]) # frozen set key
print(d[None]) # null
# Note: list, set, dict are mutable but not hashable, so cannot be key. 
# But tuple, frozenset are immutable and hashable, so can be key.
