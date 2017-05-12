#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Configuration for Schrodinger Equation Solver

    # Copyright (C) 2017 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

''' Configuration for Schrodinger Equation'''

# request package
import numpy as np
import numpy.polynomial.hermite as hmt

# ==============================
#   For QHO and Coherent State
# ==============================

# Hermite polynomial
H = hmt.Hermite((0,0,0,0,0,1))
# order of Hermite polynomial
k = 5
# eigen value of annihilation operator
alpha = 3

# approximation of annihilation state
def Hermt(n, x):
    # output data
    rslt = np.zeros_like(x)
    # create superposition of n states
    for k in range(n):
        # info for Hermit polynomial
        lst = [1 if i==k else 0 for i in range(k+1)]
        # the k-th energy eigen state
        stat = 1 / np.sqrt(2**k * np.math.factorial(k)) * np.pi**-0.25 * \
                np.exp(-np.power(x, 2)/2) * hmt.Hermite(lst)(x)
        # add up with coefficient
        rslt += alpha**k * stat / np.math.factorial(k)
    # return zoomed result
    return rslt * 0.1 # np.e**(-alpha**2/2)

# ====================
#   General Settings
# ====================

# initial condition
initial = lambda x: np.exp(-np.power(x + 7.5, 2)/0.98) * np.exp(4j*x*np.pi)
    # lambda x: np.exp(-np.power(x + 7.5, 2)/0.98) * np.exp(4j*x*np.pi)
    # lambda x: np.exp(-np.power(x - 0.5, 2)/0.01) * np.exp(5j*x*np.pi)
    # lambda x: 1 / np.sqrt(2**k * np.math.factorial(k)) * np.pi**-0.25 * \
    #                np.exp(-np.power(x, 2)/2) * H(x)
    # lambda x: Hermt(16, x)
    # lambda x: 0.02 * np.exp(-np.power(x, 2)/2) * H(x)
    # lambda x: np.pi * np.exp(-np.power(x - 0.5, 2)/0.01)
    # lambda x: np.pi * np.exp(-np.power(x - 0.1, 2)/0.004)
    # lambda x: np.sqrt(2)*np.exp(5j*x*np.pi/1.02)

# potential field
potential = lambda x: [0.0 if i < 0.0 or i > 2 else 70.0 for i in x]
    # lambda x: [0.0 if i < 0.0 or i > 2 else 70.0 for i in x]
    # lambda x: 0.5 * np.power(x, 2)
    # lambda x: 0.0 * x
    # lambda x: 0.5 * np.power(x - 0.5, 2)

# boundary condition: periodic or custom
bound = (0+0j, 0+0j)
    # (0+0j, 0+0j)
    # "periodic"

# size of spacial steps
spc_size = 0.1
# size of temporal steps
tmp_size = 1e-3

# spacial range
spc_range = (-20,20)
# total recursion
rec_num = 1.256e3 * 2

# whether to save file
save = True


# ======================
#   Calculated Results
# ======================

# total number of spacial steps
spc_steps = int(round(spc_range[1] - spc_range[0]) / spc_size) + 1

# total time range
tmp_range = (0, tmp_size * rec_num)

# End of Configuration of Schrodinger Equation Solver
