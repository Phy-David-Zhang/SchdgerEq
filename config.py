#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Configuration for Schrodinger Equation Solver

    # Copyright (C) 2017 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

''' Configuration for Schrodinger Equation'''

# request package
import numpy as np


# ====================
#   General Settings
# ====================

# initial condition
initial = lambda x: np.pi * np.exp(-np.power(x - 0.5, 2)/0.01)
    # lambda x: np.pi * np.exp(-np.power(x - 0.5, 2)/0.01)
    # lambda x: np.pi * np.exp(-np.power(x - 0.1, 2)/0.004)
    # lambda x: np.sqrt(2)*np.exp(5j*x*np.pi/1.02)

# potential field
potential = lambda x: 0.0 * x
    # lambda x: 0.0 * x
    # lambda x: 0.5 * np.power(x - 0.5, 2)

# boundary condition: periodic or custom
bound = (0+0j, 0+0j)
    # (0+0j, 0+0j)
    # "periodic"

# size of spacial steps
spc_size = 0.02
# size of temporal steps
tmp_size = 1e-5

# spacial range
spc_range = (0,1)
# total recursion
rec_num = 1e4


# ======================
#   Calculated Results
# ======================

# total number of spacial steps
spc_steps = int(round(spc_range[1] - spc_range[0]) / spc_size) + 1

# total time range
tmp_range = (0, tmp_size * rec_num)

# End of Configuration of Schrodinger Equation Solver
