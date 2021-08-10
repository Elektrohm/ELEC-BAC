import numpy as np
import matplotlib.pyplot as plt


def get_array(filename):
    with open(filename, 'r') as file:
        lst = file.readlines()[3:]
        freq = np.ones(len(lst))
        gain = np.ones(len(lst))
        phase = np.ones(len(lst))
        for i in range(len(lst)):
            a, b, c = lst[i].strip().replace(',','.').split()
            freq[i], gain[i], phase[i] = float(a), float(b), float(c)
        return freq, gain, phase


def get_array_spice(filename):
    with open(filename, 'r') as file:
        lst = file.readlines()[1:]
        freq = np.ones(len(lst))
        gain = np.ones(len(lst))
        phase = np.ones(len(lst))
        for i in range(len(lst)):
            line = lst[i].strip().replace('°', '').replace('(', ' ').replace(')', ' ').replace(',', ' ').replace('dB', ' ')
            a, b, c = line.split()
            freq[i], gain[i], phase[i] = float(a), float(b), float(c)
        return freq, gain, phase


def adjust(phase):
    for i in range(len(phase)):
        phase[i] = phase[i] if phase[i] < 0 else phase[i]-360
    return phase


def plotting(freq, gain, phase, freq2, gain2, phase2):
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('freq [Hz]')
    ax1.set_ylabel('Gain [dB]', color=color)
    ax1.semilogx(freq, gain, color=color, label="Expérimental")
    plt.grid(True, which="both")

    ax1.semilogx(freq2, gain2, color=color, label="Théorique", linestyle="dashed")
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Phase [°]', color=color)  # we already handled the x-label with ax1
    ax2.semilogx(freq, phase, color=color, label="Expérimental")
    ax2.semilogx(freq2, phase2, color=color, label="Théorique", linestyle="dashed")
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.legend()
    plt.show()


if __name__ == '__main__':
    freq, gain, phase = get_array('Gain_simu.txt')
    freq2, gain2, phase2 = get_array_spice('Gain-Spice.txt')
    phase, phase2 = adjust(phase), adjust(phase2)

    print("gain expérimentale max {}dB,\ngain théorique max {}dB".format(max(gain),max(gain2)))
    plotting(freq, gain, phase, freq2, gain2, phase2)

