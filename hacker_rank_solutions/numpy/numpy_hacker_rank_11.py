import numpy

n, m = map(int, input().split())
arr1 = numpy.array([input().split() for i in range(n)], int)
print(numpy.mean(arr1, axis = 1))
print(numpy.var(arr1, axis = 0))

# numpy.set_printoptions(legacy='1.13')
print(round(numpy.std(arr1, axis = None), 11))
