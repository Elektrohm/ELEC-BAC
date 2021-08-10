import numpy as np
import matplotlib.pyplot as plt


def get_array(filename):
    with open(filename,'r') as file:
        lst = file.readlines()
        labels = lst[0].split()

        n, m = len(lst[0].split()), len(lst)
        matrix = np.zeros((n, m-1))
        index = 0

        for line in lst[1:]:
            matrix[:, index] = [float(i) for i in line.split()]
            index += 1
        return matrix, labels


if __name__ == '__main__':
    arrays, labels = get_array("NonInverting2.txt")
    time = arrays[0]
    for i in range(len(arrays)-1):
        plt.plot(time*1e3, arrays[i+1], label=labels[i+1])
    plt.xlabel("Time[ms]")
    plt.ylabel("Voltage[V]")
    plt.legend(loc="lower left")
    plt.grid()
    plt.tight_layout()
    plt.show()