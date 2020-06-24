x=int(input("Enter a number: "))

for i in range(1,x+1):
    if i%10 == 0:
        continue
    while i<=100:
        print(i)
        break
    
n=int(input("Enter a number: "))

prime_flag = True

for i in range(2,n-1):
    if n%i==0:
        prime_flag = False

if prime_flag==True:
    print(n,"is a prime number.")
elif prime_flag==False:
    print(n,"is not a prime number.")
        