import numpy as np
import matplotlib.pyplot as plt

N = 40
h = 2 * np.pi / N
v = .005
n = (1, 1000, 2000, 4000)
iter = 10000


def u(x):
    return np.exp(2 * np.sin(x))


a = u(np.linspace(0, 2 * np.pi,  num=N,endpoint=False))
b = np.zeros(N)
e = np.zeros(10000)

for val in range(iter):
    if val+1 in n:
        plt.plot(np.linspace(0, 2 * np.pi, num=N,endpoint=False), a)
        plt.title("n = " + str(val))
    for j in range(len(b)):
        b[j] += (1-3*v)*a[j]
        jl = j - 1
        jll = j - 2
        if jl < 0:
            jl+=N
        b[j]+=v*4*a[jl]
        if jll < 0:
            jll+=N
        b[j]-=v*a[jll]

    a = np.copy(b)
    b = np.zeros(N)
    e[val] = np.sqrt((1/N)*np.sum(np.square(a)))

plt.show()
plt.plot(range(10000),e)
plt.title("error")
plt.show()