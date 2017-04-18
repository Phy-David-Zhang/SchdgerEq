-- ============================================
-- Configuration of Schrodinger Equation Solver
-- ============================================
-- 
--   Copyright (C) 2017 Zhang Changkai
--   Contact via phy.zhangck@gmail.com
--   All rights reserved.
--   
--   This is the configuration file of the 
--   solver, including the initial state,
--   steps to solve 

module Configuration where

    -- real part of initial state
    real_init = [exp (-((x-0.5)**2)/0.01) | x <- [0.0, 0.02..1.0]]
    -- imaginary part of initial state
    imag_init = replicate 51 0.0

    -- 1D potential
    potential = zero
    zero = replicate 51 0.0
    gauss = [-10*exp (-((x-0.25)**2)/0.005) | x <- [0.0, 0.02..1.0]]

    -- temporal step size
    step_t = 4e-6
    -- spacial step size
    step_x = 0.02
    -- recursion times
    rec_tot = 100000 :: Int
    -- total spatial steps
    spc_tot = 51 :: Int
    -- output gap
    gap = 100 :: Int

    -- destination
    destination = "data.txt"

-- End of Configuration File of Schrodinger Solver