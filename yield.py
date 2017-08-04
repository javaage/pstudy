import sys

def gen(n):
    for i in range(3,9):
        yield i

l = gen(10)

while True:
    try:
        print(next(l))
    except StopIteration:
        break
