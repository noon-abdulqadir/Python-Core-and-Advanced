s = {30, "XYZ", 20, 10}



s.update([88,99])

print(type(s))

#print(s*3)
s.remove(30)
print(s)

f=frozenset(s)
f.remove(20)