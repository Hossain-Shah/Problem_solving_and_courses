import numpy

arr = numpy.array([input().split() for i in range(int(input().split()[0]))],int)
print(arr.transpose())
print(arr.flatten())
