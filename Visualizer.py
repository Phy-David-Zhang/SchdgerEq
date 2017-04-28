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

# switch output data: real, imag, prob, both, all
global switch
switch = "prob"

# read the data in Data.txt and store it in 
# variable "data"
cmd = "data = "
with open("Data.txt", 'r') as file:
    for line in file:
        line = line.replace(":+ ", "+1j*")
        cmd += line
        exec(cmd)

# extract imaginary and real part of the solution
imag = []
real = []
prob = []
for psi in data:
    real.append([x.real for x in psi])
    imag.append([x.imag for x in psi])
    prob.append([abs(x)**2 for x in psi])
    
# setup the corresponding spatial coordinates
x = np.linspace(0, 1, len(real[0]))

# setup plot
fig, ax = plt.subplots()
time = ax.text(.7, .5, '', fontsize=15)
line1, = ax.plot([], [], linewidth=3, color='b')
line2, = ax.plot([], [], linewidth=3, color='r')
line3, = ax.plot([], [], linewidth=3, color='k')

ax.set_xlabel("Position, $x$")
ax.set_ylabel("Wavefunction,  $\\Psi(x, t)$")
ax.set_ylim([-.8,.8])

# initialization of animation
def init():
    global switch
    
    def set1():
        line1.set_data(x, real[0])
    def set2():
        line2.set_data(x, imag[0])
    def set3():
        line3.set_data(x, prob[0])
    
    time.set_text('')
    ax.set_xlim([0,1])
    
    if switch == "real": set1()
    elif switch == "imag": set2()
    elif switch == "both": set1(); set2()
    elif switch == "prob": set3()
    elif switch == "all": set1(); set2(); set3()
    else: set3()
    
    return line1, line2, line3, time

# animation control
def animate(i):
    global switch
    
    # update the data
    def set1(i):
        line1.set_ydata(real[i])
    def set2(i):
        line2.set_ydata(imag[i])
    def set3(i):
        line3.set_ydata(prob[i])

    time.set_text("t = {0:.4f}".format(0.02*i))

    if switch == "real": set1(i)
    elif switch == "imag": set2(i)
    elif switch == "both": set1(i); set2(i)
    elif switch == "prob": set3(i)
    elif switch == "all": set1(i); set2(i); set3(i)
    else: set3(i)
    return line1, line2, line3

# perform animation
ani = animation.FuncAnimation(fig, animate,
                              np.arange(0, len(real), 1), 
                              interval=10, 
                              blit=False, 
                              init_func=init)

# show animation
plt.show()

# This is the end of visualization of solution
