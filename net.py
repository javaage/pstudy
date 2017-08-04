from urllib.request import urlopen
for line in urlopen('http://www.runoob.com/python3/python3-stdlib.html'):
#    line = line.decode('utf-8')  # Decoding the binary data to text.
    print(line)