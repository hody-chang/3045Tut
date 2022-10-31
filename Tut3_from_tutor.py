# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:01:30 2022

@author: Mi Feng
"""

import numpy as np


# define a function capable of generating the wave function which is decided by E, r0, r and thd delta_t
def hydrogen_wavefunc(E, r0, r_max, delta_t):
    ####### calculate the lengths of both series solution and PC method #######
    L0 = int(r0 / delta_t)
    L = int(r_max / delta_t)
    force = 0
    ###########################################################################

    ############### initializing the value of a0, a1, a2, a3 ##################
    a0 = 1
    a1 = -a0
    a2 = - (1 / 6) * (E * a0 + 2 * a1)
    a3 = - (1 / 12) * (E * a1 + 2 * a2)
    ###########################################################################

    ########### regard wave function and v as a list of values ################
    wavefunc = []
    v = []
    ###########################################################################

    ######### obtain the first L0 values by series solution ###################
    for i in range(L0):
        r = i * delta_t
        wavefunc.append(a0 + a1 * r + a2 * r ** 2 + a3 * r ** 3)
        v.append(a1 + 2 * a2 * r + 3 * a3 * r ** 2)
    ###########################################################################

    ########### obtain the remaining results by using PC method ###############
    for i in range(L0, L):
        r = i * delta_t
        v.append(v[-1] + delta_t * (- 2 / r * v[-1] - (E + 2 / r) * wavefunc[-1]))
        wavefunc.append(wavefunc[-1] + delta_t * (v[-1] + v[-2]) / 2)
    ###########################################################################

    return np.array(wavefunc)


from copy import deepcopy


# define a function using the shoot method to find the eigen energy
def shooting_method(func, E1, E2, *args, **kwargs):
    ############## copy the left and right boundaries #########################
    E_left = deepcopy(E1)
    E_right = deepcopy(E2)
    ###########################################################################

    ####### calculate the last value of the func with parameter E_mid #########
    E_mid = (E_left + E_right) / 2
    res_mid = func(E_mid, *args, **kwargs)[-1]
    ###########################################################################

    #################### key part of the shooting method ######################
    while abs(res_mid) > 1e-6:
        res_left = func(E_left, *args, **kwargs)[-1]
        if res_left * res_mid > 0:
            E_left = E_mid
        else:
            E_right = E_mid
        E_mid = (E_left + E_right) / 2
        res_mid = func(E_mid, *args, **kwargs)[-1]
    ###########################################################################

    return E_mid


############################### An example ####################################
r0, r_max, delta_t = 0.01, 50, 0.001
r_arr = np.arange(0, r_max, delta_t)

analytical_wavefuncs = [np.exp(-r_arr),
                        (1 - r_arr / 2) * np.exp(- r_arr / 2),
                        (1 - r_arr * 2 / 3 + 2 / 27 * r_arr ** 2) * np.exp(-r_arr / 3)]
E = shooting_method(hydrogen_wavefunc, -0.26, -0.23, r0, r_max, delta_t)
numerical_wavefunc = hydrogen_wavefunc(E, r0, r_max, delta_t)

import matplotlib.pyplot as plt

plt.plot(r_arr, numerical_wavefunc, 'x', markevery=500)
plt.plot(r_arr, analytical_wavefuncs[1])
plt.xlabel('r')
plt.ylabel('R(r)')
plt.show()
###############################################################################












