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

    -- temporal step size
    step_t = 0.015
    -- spacial step size
    step_x = 0.02
    -- recursion times
    rec_tot = 50000 :: Int
    -- output gap
    gap = 20 :: Int

    -- destination
    destination = "data.txt"

-- End of Configuration File of Schrodinger Solver