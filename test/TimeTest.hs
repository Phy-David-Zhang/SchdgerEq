import Control.DeepSeq

real_init = [exp (-((x-0.5)**2)/0.01) | x <- [0.0, 0.02..1.0]]
imag_init = replicate 51 0.0
main = print $ last (solve real_init imag_init 0.02 25000)

double :: [Double] -> [Double]
double xs = [x*2 | x <- xs]

laplace :: [Double] -> [Double]
laplace xs = 0.0:zipWith (-)
    (zipWith (+) (init (init xs)) (tail (tail xs)))
    ([x*2 | x <- (tail (init xs))]) ++ [0.0]


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

solve :: [Double] -> [Double] -> Double -> Int -> [[[Double]]]
solve _ _ _ 0 = []
solve real imag step tot = 
    flash : solve (head flash) (last flash) step (tot-1) where
        flash = force (schrodinger real imag step)
