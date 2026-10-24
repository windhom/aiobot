import numpy

arr = numpy.array([1, 2, 3, 4, 5])
arr_2 = numpy.array([[1, 2, 3], [4, 5, 6]])

print(arr_2.reshape(5, -1))