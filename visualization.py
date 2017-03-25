# Visualization of Solution of Schrodinger Equation
# =================================================
#
#   Copyright (C) 2017 Robert Brown, Changkai Zhang
#   Contact via phy.zhangck@gmail.com
#   All rights reserved.

# This is the visualizaiton of the solution gained
# by Schrodinger equation solve engine.

# import numpy and plot library
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# read the data in data.txt and store it in 
# variable "data"
cmd = "data = "
with open("data.txt", 'r') as file:
	for line in file:
		cmd += line
		exec(cmd)

# extract imaginary and real part of the solution
imag = []
real = []
for psi in data:
    real.append(psi[0])
    imag.append(psi[1])
    
# setup the corresponding spatial coordinates
x = np.linspace(0, 1, len(real[0]))

# setup plot
fig, ax = plt.subplots()
time = ax.text(.7, .5, '', fontsize=15)
line1, = ax.plot([], [], linewidth=3, color='b')
line2, = ax.plot([], [], linewidth=3, color='r')

ax.set_xlabel("Position, $x$")
ax.set_ylabel("Wavefunction,  $\\Psi(x, t)$")
ax.set_ylim([-.8,.8])

# initialization of animation
def init():
    line1.set_data(x, real[0])
    line2.set_data(x, imag[0])
    time.set_text('')
    ax.set_xlim([0,1])
    return line1, line2, time

# animation control
def animate(i):
    line1.set_ydata(real[i])  # update the data
    line2.set_ydata(imag[i]) 
    time.set_text("t = {0:.4f}".format(0.02*i))
    return line1, line2

# perform animation
ani = animation.FuncAnimation(fig, animate,
                              np.arange(0, len(real), 3), 
                              interval=10, 
                              blit=False, 
                              init_func=init)

# show animation
plt.show()

# This is the end of visualization of solution
