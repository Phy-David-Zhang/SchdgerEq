## Schrodinger Equation Solver

This project aims to build a universal solver of Schrodinger equation in Haskell. This program is supposed to solve the Schrodinger equation with arbitrary potential and initial state.

```
    Author: Zhang Chang-kai
    Contact: phy.zhangck@gmail.com
```

Copyright (C) 2017 Zhang Chang-kai. All Rights Reserved.

### Usage

Makefile is provided for generating solutions and performing visualizations. Use `make` or `make data` to generate the solutions which will be stored in data.txt, and `make visual` will generate the animation.

The solver is written in Haskell and the visualization is accomplished through Python. Thus, GHC and Python are needed to run this program.

### Configuration

All the configurations are within file Configuration.hs, including

- `real_init` and `image_init`: the initial state
- `potential`: the potential in the equation
- `step_t` and `step_x`: temporal and spatial step size
- `rec_tot` and `src_tot`: total number of temporal and spatial steps
- `gap`: frame rate, e.g. `gap=10` means output state every 10 recursions.

### Errors of Calculation

This program uses explicit Runge-Kutta method to perform numerical simulations. As all the explicit methods, the error will accumulate and the program will fail after significantly long time. Therefore, the ratio of temporal and the square of spatial step size should be adjusted according to the total number of recursion.