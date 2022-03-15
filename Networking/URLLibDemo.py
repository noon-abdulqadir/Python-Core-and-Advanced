import urllib.request

try:
    url = urllib.request.urlopen("https://www.python.org/")
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print("The webpage is not found.")
    exit()

with open("python.html","wb") as f:
    f.write(content)