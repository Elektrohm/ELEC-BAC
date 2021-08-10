import numpy as np
import sympy as sp
from matplotlib import pyplot as plt
from scipy.signal import butter,filtfilt


DATA = np.load('angle.npz')
DATA_c = np.load('calib0.npz')

chirp = DATA['chirp']
frames = DATA['data']
background = DATA['background']

chirp_c = DATA_c['chirp']
frames_c = DATA_c['data']
background_c = DATA_c['background']

f0 = chirp[0]""
B = chirp[1]
Ns = chirp[2]
Nr = chirp[3]
Ts = chirp[4]
Tr = chirp[5]


#print(DATA['data'])

def vToM(vect, Nr, Ns, k, r_b=True, b=None):
    rep = np.zeros((int(Nr), int(Ns)), dtype=np.complex_)
    for i in range((int(Nr))):
        for j in range(int(Ns)):
            if r_b:
                rep[i][j] = vect[i*int(Ns) + j] - b[k][0][i][j]
            else:
                rep[i][j] = vect[i*int(Ns) + j]
    return rep

def butter_lowpass_filter(data, cutoff, fs, order, nyq):
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

mats = np.zeros(((4, 10, int(Nr)*int(Ns))), dtype=np.complex_) # I1, Q1, I2, Q2
mats_c = np.zeros(((4, 10, int(Nr)*int(Ns))), dtype=np.complex_) # I1, Q1, I2, Q2
back = np.zeros((((4, 10, int(Nr), int(Ns)))), dtype=np.complex_)

for k in range(len(background)):
    for i in range(len(background[0])):
        back[k][i] = vToM(background[k][i], Nr, Ns, k, r_b=False)

## Removing the background
for k in range(len(frames)):
    for i in range(len(frames[0])):
        mats[k][i] = frames[k][i] - background[k][i]
        mats_c[k][i] = frames_c[k][i] - background_c[k][i]

s_t = np.zeros(((2, 10, int(Nr)*int(Ns))), dtype=np.complex_) # S_1(t) | s_2(t)
s_t_I_Q = np.zeros(((4, 10, int(Nr)*int(Ns))), dtype=np.complex_) # S_1(t)*S_I1(t) | S_1(t)*S_Q1(t) | S_2(t)*S_I2(t) | S_2(t)*S_Q2(t)
low_pass_data = np.zeros(((4, 10, int(Nr)*int(Ns))), dtype=np.complex_)

s_t_c = np.zeros(((2, 10, int(Nr)*int(Ns))), dtype=np.complex_) # S_1(t) | s_2(t)
s_t_I_Q_c = np.zeros(((4, 10, int(Nr)*int(Ns))), dtype=np.complex_) # S_1(t)*S_I1(t) | S_1(t)*S_Q1(t) | S_2(t)*S_I2(t) | S_2(t)*S_Q2(t)
low_pass_data_c = np.zeros(((4, 10, int(Nr)*int(Ns))), dtype=np.complex_)

## Computing s(t) = s_I(t)*cos(2pi*f*t) + s_Q(t)*sin(2pi*f*t)
for k in range(len(s_t)):
    for i in range(len(s_t[0])):
        for j in range(len(s_t[0][0])):
                s_t[k][i][j] = mats[2*k][i][j] * np.cos(2*np.pi*f0*i*Ts)\
                                + mats[(2*k) + 1][i][j] * np.sin(2*np.pi*f0*i*Ts)
                s_t_c[k][i][j] = mats_c[2*k][i][j] * np.cos(2*np.pi*f0*i*Ts)\
                                + mats_c[(2*k) + 1][i][j] * np.sin(2*np.pi*f0*i*Ts)

for k in range(len(s_t)):
    for i in range(len(s_t_I_Q[0])):
        for j in range(len(s_t_I_Q[0][0])):
                s_t_I_Q[2*k][i][j] = s_t[k][i][j] * mats[2*k][i][j]
                s_t_I_Q[(2*k) + 1][i][j] = s_t[k][i][j] * mats[(2*k) + 1][i][j]
                s_t_I_Q_c[2*k][i][j] = s_t_c[k][i][j] * mats_c[2*k][i][j]
                s_t_I_Q_c[(2*k) + 1][i][j] = s_t_c[k][i][j] * mats_c[(2*k) + 1][i][j]




#y = butter_lowpass_filter(data, cutoff = 1.5*f0, fs, order, nyq = 0.5 * fs)

for k in range(len(low_pass_data)): # I_1, Q_1, I_2, Q_2
    for i in range(len(low_pass_data[0])): # 10 frames
        low_pass_data[k][i] = butter_lowpass_filter(s_t_I_Q[k][i], cutoff = f0/2000000, fs=1/Ts, order=2, nyq = 0.5 * (1/Ts))
        low_pass_data_c[k][i] = butter_lowpass_filter(s_t_I_Q_c[k][i], cutoff = f0/2000000, fs=1/Ts, order=2, nyq = 0.5 * (1/Ts))

#print(s_t_I_Q[0][0])
#print(low_pass_data[0][0])
#print(low_pass_data[1][0])
phi = np.zeros(((2, 10, int(Nr)*int(Ns))))
phi_c = np.zeros(((2, 10, int(Nr)*int(Ns))))

for k in range(2): # (I_1, Q_1), (I_2, Q_2)
    for i in range(len(low_pass_data[0])): # 10 frames
        for j in range(len(low_pass_data[0][0])):
            phi[k][i][j] = np.arctan(low_pass_data[2*k][i][j] / low_pass_data[(2*k) + 1][i][j])
            phi_c[k][i][j] = np.arctan(low_pass_data_c[2*k][i][j] / low_pass_data_c[(2*k) + 1][i][j])

f = 9

#plt.plot(np.arange(0, len(low_pass_data[0][0])), low_pass_data[0][0])
#plt.plot(np.arange(0, len(low_pass_data[0][0])), low_pass_data[1][0])
plt.plot(np.arange(0, len(low_pass_data[0][0])), phi[0][f] - phi_c[0][f])
plt.plot(np.arange(0, len(low_pass_data[0][0])), [np.mean(phi[0][f]) for i in range(len(low_pass_data[0][0]))])
plt.show()

'''
    1. Calculer s(t)*s_I(t) et s(t)*s_Q(t)
    2. Filtre passe bas sur les deux pour obtenir m_I(t) et m_Q(t)
    3. calculer tg(phi) = m_I(t) / m_Q(t)
    4. phi = arctg(m_I(t) / m_Q(t))
    5. Dodo

'''
