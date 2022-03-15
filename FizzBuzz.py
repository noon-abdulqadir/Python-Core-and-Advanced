for i in range(1,101):
    
    mulOf3 = i % 3 == 0
    mulOf5 = i % 5 == 0

    if mulOf3 and mulOf5:
        print("FizzBuzz")
    elif mulOf3:
        print("Fizz")
    elif mulOf5:
        print("Buzz")
    else:
        print(i)
