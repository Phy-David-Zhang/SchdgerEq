#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Visualization of Solution of Schrodinger Equation

    # Copyright (C) 2017 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Schrodinger Equation Solution Visulizer'''

# import dependencies
import config
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


# solution of Schrodinger equation
global sol


# set the solution
def set_sol(solution):
    global sol
    sol = solution


# generate animation
def genAnimate():

    global sol

    # set the plot of the results
    fig, ax = plt.subplots(2)
    time = ax[0].text(.7, .5, '', fontsize=15)
    line1, = ax[0].plot([], [], linewidth=3, color='b')
    line2, = ax[0].plot([], [], linewidth=3, color='r')
    line3, = ax[1].plot([], [], linewidth=1, color='k')

    # wave function
    ax[0].set_xlabel("Position, $x$")
    ax[0].set_ylabel("Wavefunction,  $\\Psi(x, t)$")
    ax[0].set_ylim([-.8,.8])
    ax[0].set_ylim([-2,2])
    ax[0].set_xlim([0,1])

    # probability density function
    ax[1].set_xlabel("Position, $x$")
    ax[1].set_ylabel("Probability density,  $|\\Psi(x, t)|^2$")
    ax[1].set_ylim([-.8,.8])
    ax[1].set_ylim([0,6])
    ax[1].set_xlim([0,1])

    def init():
        line1.set_data(sol.x,sol.psi[0].real)
        line2.set_data(sol.x,sol.psi[0].imag)
        line3.set_data(sol.x,sol.pbd[0])
        return line1, line2, line3

    def animate(i):
        line1.set_ydata(sol.psi[i].real)  # update the data
        line2.set_ydata(sol.psi[i].imag)
        line3.set_data(sol.x,sol.pbd[i])
        time.set_text("t = {0:.4f}".format(config.tmp_size*i))
        return line1, line2, line3, time

    ani.FuncAnimation(fig,
                      animate,
                      np.arange(0, sol.nt,30),
                      interval=10,
                      blit=False,
                      init_func=init)

    plt.show()

# End of Schrodinger Equation Solution Visulizer
