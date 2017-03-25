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
module SchdgerEngine where

-- import function "force" for force evaluation
import Control.DeepSeq

-- double every element of a list
double :: [Double] -> [Double]
double xs = [x*2 | x <- xs]

-- 1D laplace operator
laplace :: [Double] -> [Double]
laplace xs = 0.0:zipWith (-)
    (zipWith (+) (init (init xs)) (tail (tail xs)))
    (double (tail (init xs))) ++ [0.0]

-- Runge-Kutta method of explicit integration
schrodinger :: [Double] -> [Double] -> Double -> [[Double]]
schrodinger real imag step =
    [zipWith (+) real [step * x / 6 | x <- zipWith (+) realk1
        (zipWith (+) (double realk2) (zipWith (+) (double realk3) realk4))]] ++
    [zipWith (+) imag [step * x / 6 | x <- zipWith (+) imagk1
        (zipWith (+) (double imagk2) (zipWith (+) (double imagk3) imagk4))]]
    where
        realk1 = [-0.5 * ix | ix <- laplace imag]
        imagk1 = [ 0.5 * rx | rx <- laplace real]
        realk2 = [-0.5 * ix | ix <- laplace
            (zipWith (+) imag [step * x / 2 | x <- realk1])]
        imagk2 = [ 0.5 * rx | rx <- laplace
            (zipWith (+) real [step * x / 2 | x <- imagk1])]
        realk3 = [-0.5 * ix | ix <- laplace
            (zipWith (+) imag [step * x / 2 | x <- realk2])]
        imagk3 = [ 0.5 * rx | rx <- laplace
            (zipWith (+) real [step * x / 2 | x <- imagk2])]
        realk4 = [-0.5 * ix | ix <- laplace
            (zipWith (+) imag [step * x | x <- realk3])]
        imagk4 = [ 0.5 * rx | rx <- laplace
            (zipWith (+) real [step * x | x <- imagk3])]

-- solve the equation and push the solution into the list
solve :: [Double] -> [Double] -> Double -> Int -> [[[Double]]]
solve _ _ _ 0 = []
solve real imag step tot = 
    flash : solve (head flash) (last flash) step (tot-1) where
        flash = force (schrodinger real imag step)

-- this is the end of solve engine for Schrodinger equation

