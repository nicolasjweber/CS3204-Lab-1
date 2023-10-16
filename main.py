#!/usr/bin/env python
import numpy
import timeit


def matrix_multiplication(n):
    A = numpy.random.randint(0, 99, (n, n))
    B = numpy.random.randint(0, 99, (n, n))
    C = numpy.matmul(A, B)


if __name__ == '__main__':
    execution_times = []
    lower_bound = 2
    upper_bound = 120
    number = 1000
    for n in range(lower_bound, upper_bound):
        execution_times.append(timeit.timeit("matrix_multiplication(n)", globals=globals(), number=number) / number)
    numpy.savetxt("execution_times_~.txt", execution_times)
