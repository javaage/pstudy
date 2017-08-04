import urllib.request as request

f = request.urlopen("https://www.douyu.com")
print(f.read())