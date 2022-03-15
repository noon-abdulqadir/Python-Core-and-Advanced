x=int(input("Enter a number: "))

for i in range(1,x+1):
    if i%10 == 0:
        continue
    while i<=100:
        print(i)
        break

n=int(input("Enter a number: "))

prime_flag = all(n%i != 0 for i in range(2, n-1))
if not prime_flag:
    print(n,"is not a prime number.")
else:
    print(n,"is a prime number.")
        