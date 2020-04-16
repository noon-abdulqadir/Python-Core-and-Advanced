f = open("myfile.txt","w")
print("Enter text (type # when you are done): ")

s = ""
while s!="#":
    s = input()
    f.write(s+"\n")

f.close()

with open ("myfileopen.txt","w") as f:
    s = input("Enter text: ")
    f.write(s)
    #f.close() with statement no need to close the file