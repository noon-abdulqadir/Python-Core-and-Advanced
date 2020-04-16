lst=[10,20,"noon",-10,20.5]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))

lst.append(40)
lst.remove("noon")
del(lst[1])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))
lst.insert(3, 99)
print(lst)

print(lst[::-1])
lst.sort(reverse=True)
lst.extend([4])
print(lst)
print(lst[::-1])

countries_lst = ["sudan","netherlands","malaysia","spain"]
countries_lst.append("italy")
print(countries_lst)

del(countries_lst[3])
print(countries_lst)

x=int(len(countries_lst)/2)
countries_lst.insert(x,"austria")
print(countries_lst)