import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

# 1a)

a0 = 1
a1 = -a0
E = 1.2
a2 = a0*(2-E)/6
a3 = -a0*(1-2*E)/18
r0 = 0.01
dr = 0.0001
r = np.arange(start=0, stop=r0, step=dr)
R = np.empty_like(r)
e = np.empty_like(r)
v = np.empty_like(r)
for i in range(r.size):
    R[i] = a0 + a1*r[i] + a2*(r[i]**2) + a3*(r[i]**3)
    e[i] = np.exp(-r[i])
    v[i] = a1+2.0*a2*r[i]+3*a3**2
'''
print(r.size)
plt.plot(r, R, label="Series Solution")
plt.plot(r, e, label="exact Solution")
plt.legend()
plt.show()
'''

# 1b) shooting method


L = 10
r2 = np.arange(start=0.01, stop=L+dr, step=dr)
R2 = np.zeros(np.shape(r2), dtype="float")
e2 = np.zeros(np.shape(r2), dtype="float")
v2 = v[-1]
R2[0] = R[-1]
force = -2*v2/r2[0]-(E+2/r2[0])*R2[0]

for i in range(1, r2.size):
    R_pre = R2[i-1] + v2*dr
    v_pre = v2+force*dr
    R2[i] = R2[i-1] + 0.5*(v2+v_pre)*dr
    force_new = -2*v_pre/r2[i]-(E+2/r2[i])*R_pre
    v = v+0.5*(force+force_new)*dr
    force = force_new

print(force)
plt.plot(r2, R2, label="Shooting(E0=-1)")
plt.legend()
plt.show()
