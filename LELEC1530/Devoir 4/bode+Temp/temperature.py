import numpy as np
import matplotlib.pyplot as plt


def get_array(filename):
    with open(filename, 'r') as file:
        lst = file.readlines()[5:]
        y1, y2, t = np.ones(len(lst)), np.ones(len(lst)), np.ones(len(lst))
        t_0 = float(lst[0].split()[1].split(',')[1])

        for i in range(len(lst)):
            line = lst[i].replace(",", '.').replace("E", 'e')
            y1[i] = float(line.strip().split()[2])
            y2[i] = float(line.strip().split()[5])
            t[i] = float(line.split()[1].split('.')[1])

        return y1, y2, t-t_0


if __name__ == '__main__':
    y_1, y_2, t1 = get_array("sin_200_0.2.txt")
    y_1chaud, y_2chaud, t2 = get_array("sin_200_0.2chaud.txt")

    mean_1, mean_2 = np.mean(y_1), np.mean(y_2)
    mean_1chaud, mean_2chaud = np.mean(y_1chaud), np.mean(y_2chaud)

    print(f"Vc = {mean_2:.4f}, Vc chauffé = {mean_2chaud:.4f}")

    plt.figure()
    # 10**-3 to convert into ms
    plt.plot(t1*10**-3, y_1, label="In")
    plt.plot(t1*10**-3, y_2, label="Out")
    plt.plot(t2*10**-3, y_1chaud, label="In chaud")
    plt.plot(t2*10**-3, y_2chaud, label="Out chaud")
    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    plt.grid()
    plt.legend()
    plt.show()