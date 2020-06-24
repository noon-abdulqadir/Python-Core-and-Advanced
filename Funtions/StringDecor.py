def decorfun(hello):
    def inner(name):
        result = hello(name)
        result+=" How are you?"
        return result
    return inner

@decorfun
def hello(name):
    return "Hello "+name

print(hello("Noon"))