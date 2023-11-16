import numpy as np
import matplotlib.pyplot as plt

m = 512
h = (2 * np.pi) / m
dt = h / 10
T = (3 * np.pi) / np.sqrt(5)
snaps = (0,.25*T, .5*T, .75*T, T)

def A(x):
    return 2 + (4 / 3) * np.sin(x)


def q(x):
    return np.exp(np.sin(x) + (1 / 2) * np.sin(4 * x))


Q = q((np.linspace(0, m - 1, m) + 1 / 2) * h)
A_full = A((np.linspace(0, m - 1, m) + 1 / 2) * h)
A_stag = A(np.linspace(0, m - 1, m) * h)
F_left = np.zeros(m)
F_right = np.zeros(m)
t = 0
curr = 0
while t < T:
    if t >= snaps[curr]:
        plt.plot(np.linspace(0,m-1,m),Q)
        plt.title(str(snaps[curr]/T) + " T")
        plt.show()
        curr+=1
    for i in range(m):
        il = i - 1
        if il < 0:
            il += m
        F_left[i] = (A_full[il] * Q[il] + A_full[i] * Q[i]) / 2 - (A_stag[i] * dt) / (2 * h) * (
                    A_full[i] * Q[i] - A_full[il] * Q[il])

        ir = i + 1
        if ir > m - 1:
            ir -= m
        F_right[i] = (A_full[i] * Q[i] + A_full[ir] * Q[ir]) / 2 - (A_stag[ir] * dt) / (2 * h) * (
                    A_full[ir] * Q[ir] - A_full[i] * Q[i])

    Q = Q - (dt/h)*(F_right - F_left)
    t+=dt
plt.plot(np.linspace(0,m-1,m),Q)
plt.title(str(snaps[curr]/T) + " T")

plt.show()
