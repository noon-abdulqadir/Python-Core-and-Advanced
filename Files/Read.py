import os,sys

if os.path.isfile("myfile.txt"):
    with open("myfile.txt","r") as f:
        s = f.read()
        print(s)
else:
    print("File does not exist.")
    sys.exit()