import numpy

n, m = map(int, input().split())
arr1 = numpy.array([input().split() for i in  range(n)], int)
print(numpy.max(numpy.min(arr1, axis = 1)))
