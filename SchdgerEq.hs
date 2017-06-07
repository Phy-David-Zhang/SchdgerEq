-- =====================================
-- Solve Engine for Schrodinger Equation 
-- =====================================
--
--   Copyright (C) 2017 Zhang Changkai
--   Contact via phy.zhangck@gmail.com
--   All rights reserved.
--
--   This is the main file for solving 
--   Schrodinger equation numerically
--   through classical Runge-Kutta method.

-- provide module SchdgerEngine
module SchdgerEq where

-- import function "force" for force evaluation
import Control.DeepSeq
-- import complex support
import Data.Complex
-- import configuration
import Configure

-- double every element of a list
double :: [Complex Double] -> [Complex Double]
double xs = [x*2 | x <- xs]

-- 1D hamiltonian
hamiltonian :: [Complex Double] -> [Complex Double]
hamiltonian xs = zipWith (-) potential (laplace xs) 

-- 1D laplace operator
laplace :: [Complex Double] -> [Complex Double]
laplace xs = (0.0:+0.0):(central xs (spc_tot-1))

-- 1D central difference
central :: [Complex Double] -> Int -> [Complex Double]
central xs 1 = [0.0:+0.0]
central xs n = (l+r-2*c)/(step_x:+0.0)**2:(central (tail xs) (n-1))
    where (l:c:r:_) = xs

-- Runge-Kutta method of explicit integration
schrodinger :: [Complex Double] -> Double -> [Complex Double]
schrodinger init step =
    zipWith (+) init [(step:+0.0) * x / 6 | x <- zipWith (+) first 
        (zipWith (+) (double secnd) 
        (zipWith (+) (double third) forth))]
    where
        first = [(0.0:+(-1.0)) * x | x <- hamiltonian init]
        secnd = [(0.0:+(-1.0)) * x | x <- hamiltonian
            (zipWith (+) init [(step:+0.0) * x / 2 | x <- first])]
        third = [(0.0:+(-1.0)) * x | x <- hamiltonian
            (zipWith (+) init [(step:+0.0) * x / 2 | x <- secnd])]
        forth = [(0.0:+(-1.0)) * x | x <- hamiltonian
            (zipWith (+) init [(step:+0.0) * x | x <- third])]

-- solve the equation and push the solution into the list
solve :: [Complex Double] -> Double -> Int -> [[Complex Double]]
solve _ _ 0 = []
solve init step tot = 
    flash : solve flash step (tot-1) where
        flash = force (schrodinger init step)

-- this is the end of solve engine for Schrodinger equation
