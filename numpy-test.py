from numpy import *

a = arange(24)
b = a.reshape((2,3,4))

a = arange(30)
a.shape = 2,-1,4  # -1 means "whatever is needed"
print(a.shape)


#print(b.T)

# c = b > 4
# print(c)
#
# print(b[c])


# print(b)
# print(b[1,0:2,3])

# print(b)
# print(b.shape)
# print(b.ndim)
# print(b.itemsize)
# print(b.size)
# print(b.dtype)
# print(type(a))
# print(type(b))
#
# c=array([2,3,4])
