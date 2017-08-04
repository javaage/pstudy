import jsontest

f=open("test.json","r")
data = jsontest.load(f)
print(data["name"])


num = 100

for i in range(2,100):
    for j in range(2,int(i/2)):
        if(i%j==0):
            break
        print(i)
        break
