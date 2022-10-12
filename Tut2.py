import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


n_inter = 10000
dt = 0.0005
theta = np.zeros(n_inter)
t = np.arange(0, n_inter * dt, dt)

theta[0] = np.pi / 2

v = np.zeros(n_inter)
a = np.zeros(n_inter)
d = np.zeros((n_inter, 2))

for i in range(n_inter - 1):
    a[i] = -9.81 * np.sin(theta[i])
    v[i + 1] = v[i] + a[i] * dt
    theta[i + 1] = theta[i] + v[i] * dt
    d[i] = [np.cos(theta[i]-np.pi/2), np.sin(theta[i]-np.pi/2)]
'''
plt.plot(t, theta, label = "Angle")
plt.plot(t, v, label = "Angular velocity")
plt.plot(t, a, label = "Acc")
plt.xlabel("Time")
plt.legend()
plt.show()
'''

# Animation

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-1, 1), ylim=(-1, 1.))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '.-', lw=1, ms=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def animate(i):

    line.set_data([0, d[i, 0]], [0, d[i, 1]])
    time_text.set_text(time_template % (i*dt))
    return line, trace, time_text

animation = FuncAnimation(
    fig, animate, len(d), interval=dt*100, blit=True)
plt.show()
