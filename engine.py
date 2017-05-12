#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Engine for Numerical Schrodinger Equation Solver

    # Copyright (C) 2017 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Numerical Schrodinger Equation Solve Engine'''

# Principle of Calculation
# ========================
#
# This program solves 1D Schrodinger equation through brute-force integrat-
# ion by Crank-Nicolson numetrical integration method. The Schrodinger equ-
# ation reads
#                    iħ ∂ψ/∂t = - ħ²/2m ∂²ψ/∂x² + Vψ
# In this program, physical constants are neglected. Thus, the actual equa-
# tion solved is
#                     i ∂ψ/∂t = - ∂²ψ/∂x² + Vψ
# To solve this equation, first transform the equation into discrete form
#    ψ(x,t+1) - ψ(x,t) = r/2 (ψ(x-1, t+1) + ψ(x+1, t+1) - 2ψ(x, t+1))
#                      + r/2 (ψ(x-1, t) + ψ(x+1, t) - 2ψ(x, t))
#                      - iV Δt ψ(x,t)
# where r = i Δt / 2Δx². This formula is the Crank-Nicolson method. Written
# in matrix form
#
#  ⎡1+2r  -r                        ⎤ ⎡  ψ(1,t+1)  ⎤
#  ⎜ -r  1+2r  -r                   ⎟ ⎜  ψ(2,t+1)  ⎟
#  ⎜      -r  1+2r  -r              ⎟ ⎜  ψ(3,t+1)  ⎟
#  ⎜                                ⎟ ⎜            ⎟
#  ⎜                                ⎟ ⎜            ⎟
#  ⎜                  -r  1+2r  -r  ⎟ ⎜ ψ(n-1,t+1) ⎟
#  ⎣                       -r  1+2r ⎦ ⎣  ψ(n,t+1)  ⎦
#
#                   ⎡1-2r  r                       ⎤ ⎡  ψ(1,t)  ⎤
#                   ⎜ r  1-2r  r                   ⎟ ⎜  ψ(2,t)  ⎟
#                   ⎜      r  1-2r  r              ⎟ ⎜  ψ(3,t)  ⎟
#               =   ⎜                              ⎟ ⎜          ⎟
#                   ⎜                              ⎟ ⎜          ⎟
#                   ⎜                  r  1-2r  r  ⎟ ⎜ ψ(n-1,t) ⎟
#                   ⎣                      r  1-2r ⎦ ⎣  ψ(n,t)  ⎦
#
# The potential is expressed as a diagonal matrix and is not presented here.
# This is the basic principle of this engine.
#


# import dependencies
import numpy as np
from config import *


# class of methods for Schrodinger equation Solver
# read the configuration from config.py

class Schdger(object):

    # initialization according to configuration from config.py
    def __init__(self):

        # spacial step size
        self.dx = spc_size
        # temporal step size
        self.dt = tmp_size
        # total spacial steps
        self.nx = spc_steps
        # total temporal steps
        self.nt = int(rec_num)

        # integration parameter
        self.r = 0.25j * self.dt / self.dx**2

        # set coordinates
        self.x = np.linspace(spc_range[0], spc_range[1], self.nx)

        # initialize wave function ψ(t,x)
        self.psi = np.empty([self.nt, self.nx], dtype=complex)
        # initialize probability density
        self.pbd = np.empty([self.nt, self.nx], dtype=float)

        # set potential
        self.potential = potential(self.x)

        # initial condition
        self.psi[0] = initial(self.x)
        self.pbd[0] = np.power(self.psi[0].real, 2) \
                    + np.power(self.psi[0].imag, 2)

        # boundary conditions
        self.periodic = True if bound == "periodic" else False
        self.boundary = bound if not self.periodic else None


    # generate matrices
    def _genMatrix(self):

        side = (self.nx-1) * [self.r,]
        main = self.nx * [1-2*self.r,]

        return np.diag(side, k=1) + np.diag(side, k=-1) \
                + np.diag(main, k=0)


    # generate boundary conditions
    def _genBoundary(self, i):

        if not self.periodic:
            self.psi[i, 0] = self.boundary[0]
            self.psi[i, -1] = self.boundary[1]


    # generate transitional matrix
    def _genTrans(self):

        # generate basic form
        self.trans = self._genMatrix()

        # apply periodic boundary conditions
        if self.periodic:
            self.trans[-1,0] = -self.r
            self.trans[0,-1] = -self.r

        # apply potential
        self.trans -= 0.5j * self.dt * np.diag(self.potential)

        # generate backward matrix
        self.frans = np.conjugate(self.trans)


    # solve the equation
    def solveEq(self):

        # generate transitional matrix
        self._genTrans()

        # integration
        for i in range(self.nt-1):
            # set boundary conditions
            self._genBoundary(i)
            self.psi[i+1] = \
                np.linalg.solve(self.frans, np.dot(self.trans, self.psi[i]))
            self.pbd[i+1] = np.power(self.psi[i].real, 2) \
                          + np.power(self.psi[i].imag, 2)

# End of Engine for Numerical Schrodinger Equation Solver
