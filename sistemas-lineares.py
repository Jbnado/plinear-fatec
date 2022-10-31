import numpy

A = numpy.matrix(
    [
        [1, 2, 3],
        [2, 2, 4],
        [4, 2, 5]
    ]
)

b = numpy.matrix(
    [
        [1],
        [0],
        [6]
    ]
)

x = numpy.linalg.inv(A) * b

print(x)
