x=int(input("Enter a min number: "))
y=int(input("Enter a max number: "))

i=x

if i%2==0:
    i+=1
while i<=y:
    print(i)
    i+=2