#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Interface for Numerical Schrodinger Equation Solver

    # Copyright (C) 2017 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Numerical Schrodinger Equation Solve Interface'''

# import engine and Visualization
import engine
import visual

# designate action
control = "animate"

_genSolution = engine.Schdger()
_genSolution.solveEq()

if control == "animate":
    visual.set_sol(_genSolution)
    visual.genAnimate()

# End of Interface for Schrodinger Equation Solver
