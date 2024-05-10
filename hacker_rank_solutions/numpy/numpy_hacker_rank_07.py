import numpy

n, m = map(int, input().split())
arr1 = numpy.array([input().split() for i in range(n)], int)
arr2 = numpy.array([input().split() for i in range(n)], int)
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 // arr2)
print(arr1 % arr2)
print(arr1 ** arr2)