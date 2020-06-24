dict1={1:"john",2:"bob",3:"bill"}
print(dict1)

print(dict1.items())
print(dict1.keys())
print(dict1.values())

k = dict1.keys()
for i in k:print(i)

v=dict1.values()
for i in v:print(i)

print(dict1[3])
print(list(dict1.keys())[list(dict1.values()).index("bob")])

del(dict1[2])
print(dict1)