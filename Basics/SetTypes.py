s={10,20,30,"xyz",10,20}
print(s)
print(type(s))

s.update([88,99])
print(s)

#print(s[0:5])
s.remove(30)
print(s)

f=frozenset(s)
#f.remove(20)