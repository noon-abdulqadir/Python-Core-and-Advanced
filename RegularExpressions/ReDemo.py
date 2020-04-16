import re

s = "Take 1 up 1-3-2019 One 23 idea. One idea 45 at a time Only 12-11-2020."

result = re.search(r'o\w', s)
print(result)

result = re.findall(r'o\w\w', s)
print(result)

result = re.match(r'T\w\w', s)
print(result.group())

result = re.findall(r'O\w{3}', s)
print(result)

result = re.findall(r'O\w{1,2}', s)
print(result)

result = re.findall(r'O\w?', s)
print(result)

result = re.split(r'\d+', s)
print(result)

result = re.sub(r'One','Two', s)
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', s)
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', s)
print(result)

result = re.search(r'^T\w*', s)
print(result.group())