main = print $ last (test 10000000)

test :: Int -> [Double]
test n = come xs ys where 
    xs = take n [1.1, 1.2..]
    ys = take n [2.1, 2.2..]

go :: [Double] -> [Double] -> [Double]
go [] [] = []
go (x:xs) (y:ys) = (x+y):go xs ys

come :: [Double] -> [Double] -> [Double]
come xs ys = zipWith (+) xs ys