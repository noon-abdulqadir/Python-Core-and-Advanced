for i in range(1,101):
    
    mulOf3 = True if i % 3 == 0 else False
    mulOf5 = True if i % 5 == 0 else False
    
    if mulOf3 == True and mulOf5 == True:
        print("FizzBuzz")
    elif mulOf3 == True:
        print("Fizz")
    elif mulOf5 == True:
        print("Buzz")
    else:
        print(i)