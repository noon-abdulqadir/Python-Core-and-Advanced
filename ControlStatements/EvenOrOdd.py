#x=int(input("Enter a number: "))
#if x==0:print(x,"is zero.")
#elif x%2==0:print(x,"is even.")
#else:print(x,"is odd.")

#if x:=int(input("Enter a number: "))%2==0:print(x,"is even.")
#else:print(x,"is odd.")

maths=float(input("Enter maths grade: "))
physics=float(input("Enter physics grade: "))
chemistry=float(input("Enter chemistry grade: "))

subjects = {"maths":maths,"physics":physics,"chemistry":chemistry}
min_val = min(subjects.values())

if min_val <= 35:
    for k,v in subjects.items():
        if v==min_val:
            print("You Have failed %s."% k)
elif min_val > 35:
    print("You have passed the exams.")
    av=float(maths+physics+chemistry)/3
    if av<=59:
        print("You're grade is C. Your average grade is %.2f."%av)
    elif av<=69:
        print("You're grade is B. Your average grade is %.2f."%av)
    elif av>69:
        print("You're grade is A. Your average grade is %.2f."%av)