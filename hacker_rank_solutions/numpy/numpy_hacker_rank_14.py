import numpy

p = numpy.array(input().split(), dtype = numpy.float64)
x = int(input())

print(numpy.polyval(p, x))