import numpy as np
import matplotlib.pyplot as plt

n_inter = 1000
dt = 0.005
theta = np.zeros(n_inter)
t = np.arange(0,n_inter*dt,dt)

theta[0] = np.pi/2

v = np.zeros(n_inter)
a = np.zeros(n_inter)

for i in range(n_inter-1):
    a[i] = -9.81*np.sin(theta[i])
    v[i+1] = v[i] + a[i] * dt
    theta[i+1] = theta[i] + v[i] * dt

plt.plot(t, theta, label = "Angle")
plt.plot(t, v, label = "Angular velocity")
plt.plot(t, a, label = "Acc")
plt.xlabel("Time")
plt.legend()
plt.show()

