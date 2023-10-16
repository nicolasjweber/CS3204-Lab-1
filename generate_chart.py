#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy

if __name__ == '__main__':
    execution_times_native = numpy.fromfile("execution_times_native.txt", sep="\r\n")
    execution_times_container = numpy.fromfile("execution_times_container.txt", sep="\r\n")
    execution_times_hyperv = numpy.fromfile("execution_times_hyperv.txt", sep="\r\n")
    execution_times_vm = numpy.fromfile("execution_times_vm.txt", sep="\r\n")
    lower_bound = 2
    upper_bound = 120

    plt.plot(range(lower_bound, upper_bound), execution_times_native, label="Native")
    plt.plot(range(lower_bound, upper_bound), execution_times_container, label="Container")
    plt.plot(range(lower_bound, upper_bound), execution_times_hyperv, label="Virtual Machine (Hyper-V)")
    plt.plot(range(lower_bound, upper_bound), execution_times_vm, label="Virtual Machine (VMware)")
    plt.legend()
    plt.grid()
    plt.ylabel("execution time [s]")
    plt.xlabel("matrix size n")
    plt.tight_layout()
    plt.savefig("matrix_multiplication_chart.png", dpi=400)
    plt.show()
